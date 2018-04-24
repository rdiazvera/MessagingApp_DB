from config.dbconfig import pg_config
import psycopg2


# Data Access Object (DAO) Class to access the Messages, Replies, Reactions and Hashtags entities
class MessagesDAO:

    # Initialization Method (Class Constructor)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    # === Messages Getters === #

    # List of all messages in the system
    def getAllMessages(self):
        cursor = self.conn.cursor()
       # query = "select mid, text, date_created, uid, gid from messages;"
        query = "select username, messages.mid, text, date_created, messages.uid as " \
                "author, gid, count(case when type = 'like' then 1 else null end) as like, count(case " \
                "when type='dislike' then 1 else" \
                " null end), first_name, last_name as dislike from messages, users, reactions where messages.uid " \
                "= users.uid AND messages.mid = reactions.mid group by username, messages.mid, users.first_name, " \
                "users.last_name order by date_created;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, text, date_created, uid, gid from messages where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # === Reactions Getters === #

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select uid, mid, type from reactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Number of likes to a message
    def getNumberOfLikes(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from reactions where mid = %s and type= 'like';"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # List of users who liked a message
    def getUsersWhoLikeMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email, " \
                "username from users natural inner join (select uid from " \
                "reactions natural inner join users where mid = %s and type= 'like') as P; "
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Number of dislikes to a message
    def getNumberOfDislikes(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from reactions where mid = %s and type= 'dislike';"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # List of users who dislikes a message
    def getUsersWhoDislikeMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email, username " \
                "from users natural inner join (select uid from reactions natural inner join " \
                "users where mid = %s and type= 'dislike') as P;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # === Replies Getters === #

    # === Hashtags Getters === #

from flask import jsonify, request
from dao.messagesDAO import MessagesDAO
from handler import buildDict
from handler.groupchatsHandler import GroupChatsHandler



# Handler Class to handle the Messages, Replies, Reactions and Hashtags entities
class MessagesHandler:

    # === Messages Getters === #

    # List of all messages in the system
    def getAllMessages(self):
        dao = MessagesDAO()
        result = dao.getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_all_messages_dict(self, r))
        return jsonify(Messages=mapped_result)

    def getMessageById(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageById(mid)
        mapped = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped = buildDict.build_messages_dict(self, r)
            return jsonify(Messages=mapped)


    # === Reactions Getters === #

    def getAllReactions(self):
        dao = MessagesDAO()
        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_reactions_dict(self, r))
        return jsonify(Reactions=mapped_result)

    # Number of likes to a message
    def getNumberOfLikes(self, mid):
        dao = MessagesDAO()
        result = dao.getNumberOfLikes(mid)
        mapped = []
        for r in result:
            mapped.append(buildDict.build_reaction_count_dict(self, r))
        return jsonify(Likes=mapped)

    # List of users who liked a message
    def getUsersWhoLikeMessage(self, mid):
        dao = MessagesDAO()
        result = dao.getUsersWhoLikeMessage(mid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_users_dict(self, r))
        return jsonify(Users=mapped_result)

    # Number of dislikes to a message
    def getNumberOfDislikes(self, mid):
        dao = MessagesDAO()
        result = dao.getNumberOfDislikes(mid)
        mapped = []
        for r in result:
            mapped.append(buildDict.build_reaction_count_dict(self, r))
        return jsonify(Dislikes=mapped)


    # List of users who dislikes a message
    def getUsersWhoDislikeMessage(self, mid):
        dao = MessagesDAO()
        result = dao.getUsersWhoDislikeMessage(mid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_users_dict(self, r))
        return jsonify(Users=mapped_result)

    # === PHASE 3 === #

    def addReactions(self, form):
        print(form)
        uid = form['uid']
        mid = form['mid']
        gid = form['gid']
        type = form['type']
        MessagesDAO().addReactions(uid, mid, type)
        result = buildDict.build_reaction_dict_by_attr(self, uid, mid, type)
        return GroupChatsHandler().getMessagesByGroupChatId(gid)



    #

    # === Replies Getters === #


    # === Hashtags Getters === #

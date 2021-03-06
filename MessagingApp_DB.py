from flask import Flask, request
from handler.messagesHandler import MessagesHandler
from handler.usersHandler import UsersHandler
from handler.groupchatsHandler import GroupChatsHandler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Default Route
@app.route('/')
def welcome():
    return 'Welcome to the Social Messaging App - Default Route'


# -- Phase II Routes -- #


# Route - List of all messages in the system
@app.route('/MessagingApp_DB/messages/')
def getAllMessages():
    return MessagesHandler().getAllMessages()

# Route - Number of likes to a message
@app.route('/MessagingApp_DB/messages/<int:mid>/likes/count/', methods=['GET', 'POST'])
def getNumberOfLikes(mid):
    if request.method == 'GET':
        return MessagesHandler().getNumberOfLikes(mid)
    else:
        return MessagesHandler().addReactions(request.json)

# Route - List of users who liked a message
@app.route('/MessagingApp_DB/messages/<int:mid>/likes/users/')
def getUsersWhoLikeMessage(mid):
    return MessagesHandler().getUsersWhoLikeMessage(mid)

# Route - Number of dislikes to a message
@app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/count/', methods=['GET', 'POST'])
def getNumberOfDislikes(mid):
    if request.method == 'GET':
        return MessagesHandler().getNumberOfDislikes(mid)
    else:
        return MessagesHandler().addReactions(request.json)

# Route - List of users who dislikes a message
@app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/users/')
def getUsersWhoDislikeMessage(mid):
    return MessagesHandler().getUsersWhoDislikeMessage(mid)

# Route - List of users in the contact list of some user X
@app.route('/MessagingApp_DB/users/<int:uid>/contacts/')
def getContactsOfUser(uid):
    return UsersHandler().getContactsOfUser(uid)

# Route - List of messages posted to a chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/messages/', methods=['GET', 'POST'])
def getMessagesByGroupChatId(gid):
    if request.method == 'GET':
            return GroupChatsHandler().getMessagesByGroupChatId(gid)
    else:
        return GroupChatsHandler().postMessage(gid, request.json)

@app.route('/MessagingApp_DB/groupchats/<int:gid>/hashtags/<string:hstring>')
def MessagesByHashTagInGroup(gid, hstring):
    return GroupChatsHandler().getMessagesByHashTagInGroup(gid, hstring)

# Route - List of users subscribed to a chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/users/', methods=['GET', 'POST'])
def getUsersInAGroupChat(gid):
    if request.method == 'GET':
        return GroupChatsHandler().getUsersInAGroupChat(gid)
    else:
        return GroupChatsHandler().addUsersToGroupChat(gid, request.json)

# Route - List of users in the system
@app.route('/MessagingApp_DB/users/')
def getAllUsers():
    return UsersHandler().getAllUsers()

# Route - List of chats group in the system
@app.route('/MessagingApp_DB/groupchats/')
def getAllGroupChats():
    return GroupChatsHandler().getAllGroupChats()

# Route - Owner of a given chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/owner')
def getOwnerOfGroupChat(gid):
    return GroupChatsHandler().getOwnerOfGroupChat(gid)

# Route - Information on a given user (by id)
@app.route('/MessagingApp_DB/users/<int:uid>/')
def getUserInformationById(uid):
    return UsersHandler().getUserInformationById(uid)

# Route - Information on a given user (by username)
@app.route('/MessagingApp_DB/users/<string:username>/')
def getUserInformationByUsername(username):
    return UsersHandler().getUserInformationByUsername(username)


# -- Phase III Routes -- #


@app.route('/MessagingApp_DB/GroupChats/<int:uid>/available/', methods=['GET', 'POST'])
def availableGroupChats(uid):
    if request.method == 'GET':
        return GroupChatsHandler().availableGroupChats(uid)
    else:
        print("main")
        return GroupChatsHandler().createGroupChat(uid, request.json)

@app.route('/MessagingApp_DB/users/login/', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        return UsersHandler().loginUser(request.json)

# Route - Ability to add new user

@app.route('/MessagingApp_DB/users/register/', methods=['GET', 'POST'])
def registerUser():
    if request.method == 'POST':
        return UsersHandler().registerUser(request.json)
# Route - Ability to join a chat group


# Route - List of chat groups to which a user belongs
@app.route('/MessagingApp_DB/users/<int:uid>/groupchats/')
def getGroupChatByUserId(uid):
    return UsersHandler().getGroupChatbyUserId(uid)

# Route - The ability to post a reply to a message
@app.route('/MessagingApp_DB/groupchats/<int:gid>/messages/reply', methods=['GET','POST'])
def replyToMessageGroupChatId(gid):
    if request.method == 'POST':
        return GroupChatsHandler().replyToMessage(gid, request.json)

if __name__ == '__main__':
    app.run()



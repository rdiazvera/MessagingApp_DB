angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 2;
        this.newText = "";

        this.loadMessages = function(){

            //console.log("test");
            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/";

            $http.get(url).then(
                function(response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;

                },
                function(response){
                    var status = response.status;
                    if (status == 0){
                        alert("No internet connection.");
                    }
                    else if (status == 401){
                        alert("Session Expired.");
                    }
                    else if (status == 403){
                        alert("Not authorized.");
                    }
                    else if (status == 404){
                        alert("Not Found.");
                    }
                    else {
                        alert("Internal system error.");
                    }
                });

                $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am

            var username = "EL_FELI_1924 ";
            var Name = "Felipe Santiago"
            var nextId = thisCtrl.counter++;

            var url = "/MessagingApp_DB/groupchats/2/messages/"
            var data = JSON.stringify({})
            thisCtrl.messageList.unshift({"mid": nextId, "text" : msg, "username" : username, "Name" : Name,
            "like" : 0, "dislike" : 0, "date_created": "just now"});
            thisCtrl.newText = "";
        };

        this.likeMsg = function(){
            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/2/likes/count/";
            var data = JSON.stringify({uid: 4, mid: 5, type: "like" })
            $http.post(url, data).then(

                function(response){
                    console.log(data);
                    console.log("response: " + JSON.stringify(response));
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
                    var status = response.status;
                    if (status == 0){
                        alert("No internet connection.");
                    }
                    else if (status == 401){
                        alert("Session Expired.");
                    }
                    else if (status == 403){
                        alert("Not authorized.");
                    }
                    else if (status == 404){
                        alert("Not Found.");
                    }
                    else {
                        alert("Internal system error.");
                    }
                });
        this.loadMessages();
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.dislikeMsg = function(){

            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/2/dislikes/count/";
            //"http://127.0.0.1:5000/MessagingApp_DB/messages/"+"<int:+" data[1] + ">/dislikes/count/";
            var data = JSON.stringify({uid: 3, mid: 5, type: "dislike" })
            $http.post(url, data).then(

                function(response){
                    console.log(data);
                    console.log("response: " + JSON.stringify(response));
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
                    var status = response.status;
                    if (status == 0){
                        alert("No internet connection.");
                    }
                    else if (status == 401){
                        alert("Session Expired.");
                    }
                    else if (status == 403){
                        alert("Not authorized.");
                    }
                    else if (status == 404){
                        alert("Not Found.");
                    }
                    else {
                        alert("Internal system error.");
                    }

                });
        this.loadMessages();
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.replyMsg = function(){
            alert("The \"Reply\" button is under construction.");
        };

        this.loadMessages();
}]);

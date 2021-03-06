(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/home', {
            templateUrl: 'pages/home.html',
            controller: 'HomeController',
            controllerAs : 'homeCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/groups', {
            templateUrl: 'pages/groups.html',
            controller: 'HomeController',
            controllerAs : 'homeCtrl'
            }).otherwise({
            redirectTo: '/login'
        });
    }]);

})();

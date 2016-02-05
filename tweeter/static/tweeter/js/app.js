var TweeterApp = angular.module('TweeterApp', ['ngResource'])

TweeterApp.config(['$interpolateProvider', '$httpProvider', '$resourceProvider', function($interpolateProvider, $httpProvider, $resourceProvider){
	$interpolateProvider.startSymbol('[[').endSymbol(']]');
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$resourceProvider.defaults.stripTrailingSlashes = false;
}]);

TweeterApp.controller('TweetsController', ['$scope', 'Tweet', 'AuthUser', function($scope, Tweet, AuthUser){
	
	$scope.currentUser = AuthUser;
	
	$scope.newTweetSubmit = function(text){
		if($scope.currentUser.username != ''){
			var newTweet = new Tweet;
			newTweet.text = text;
			newTweet.$save()
				.then(function(){
					$scope.allTweets.unshift(newTweet);
					$scope.newTweetText = '';
				});
		}
		else{
			console.log('Login to tweet');
		}
	};

	$scope.allTweets = Tweet.query();
}]);

TweeterApp.factory('Tweet', ['$resource', function($resource){
	return $resource("/api/tweets/:id/");
}]);

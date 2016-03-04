var TweeterApp = angular.module('TweeterApp', ['ngResource', 'ui.bootstrap']);

TweeterApp.config(['$interpolateProvider', '$httpProvider', '$resourceProvider', function($interpolateProvider, $httpProvider, $resourceProvider){
	$interpolateProvider.startSymbol('[[').endSymbol(']]');
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$resourceProvider.defaults.stripTrailingSlashes = false;
}]);

TweeterApp.controller('TweetsController', ['$scope', 'Tweet', 'AuthUser', '$uibModal', function($scope, Tweet, AuthUser, $uibModal){
	
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

	// $scope.openAuthModal = function(activeTab){
	// 	$scope.activeTab = activeTab;

	// 	var authModal = $uibModal.open({
	// 		templateUrl: '/static/tweeter/partials/auth-modal-content.html',
	// 		controller: 'AuthModalController',
	// 		resolve: {
	// 			activeTab: function(){
	// 				return activeTab;
	// 			}
	// 		}
	// 	});

	// 	authModal.result.then(function(){
	// 		$scope.activeTab = 'all-tweets';
	// 	});
	// };

}]);

// TweeterApp.controller('AuthModalController', ['$scope', '$uibModalInstance', function($scope, $uibModalInstance, activeTab){
// 	$scope.closeAuthModal = function(){
// 		$uibModalInstance.close();
// 	};
// 	$scope.activeTab = activeTab;

// }]);

TweeterApp.factory('Tweet', ['$resource', function($resource){
	return $resource("/api/tweets/:id/");
}]);



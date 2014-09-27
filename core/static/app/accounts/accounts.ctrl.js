(function (){
  var app = angular.module('Jogging.accounts.ctrl', []);

  app.controller('AccountController',
    ['$scope', 'AccountFactory', 'Restangular',
      function ($scope, AccountFactory, Restangular){
        var accountFactoryCallbacks = {};
        accountFactoryCallbacks.createAccountCallback = function(data){
          angular.extend($scope.accountCreationResponse, data);

          if (data.status === 201){
            $scope.newAccount = {};
          }else if (data.status === 400){
            angular.forEach(data.data, function(error, field){
              $scope.signupForm[field].$setValidity('', false);
            });
          }
        };

        $scope.accountCreationResponse = {};
        $scope.accountFactory = new AccountFactory(accountFactoryCallbacks);
      }
  ]);
})();

(function (){
  var app = angular.module('Jogging.accounts.ctrl', []);

  app.controller('AccountController',
    ['$scope', '$location', 'AccountFactory',
      function ($scope, $location, AccountFactory){
        var accountFactoryCallbacks = {};
        accountFactoryCallbacks.createAccountCallback = function(response){
          if (response.status === 201){
            $location.path('/timings');
          }else if (response.status === 400){
            angular.forEach(response.data, function(error, field){
              $scope.signupForm[field].$setValidity('', false);
            });
          }
        };

        $scope.accountFactory = new AccountFactory(accountFactoryCallbacks);
      }
  ]);
})();

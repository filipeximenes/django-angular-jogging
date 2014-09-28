(function (){
  var app = angular.module('Jogging.accounts.ctrl', []);

  app.controller('AccountCreateController',
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

  app.controller('LoginController',
    ['$scope', '$location', 'AccountFactory',
      function ($scope, $location, AccountFactory){
        var accountFactoryCallbacks = {};
        accountFactoryCallbacks.performLoginCallback = function(response){
          if (response.status === 200){
            $location.path('/timings');
          }else if (response.status === 400){
            $scope.loginFailure = true;
          }
        };

        $scope.accountFactory = new AccountFactory(accountFactoryCallbacks);
      }
  ]);
})();

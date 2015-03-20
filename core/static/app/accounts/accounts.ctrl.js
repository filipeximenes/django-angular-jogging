(function (){
  var app = angular.module('Jogging.accounts.ctrl', []);

  app.controller('AccountCreateController',
    ['$scope', '$location', 'AccountFactory',
      function ($scope, $location, AccountFactory){
        $scope.accountFactory = new AccountFactory({
          onCreateAccountSuccess: function (response){
            $location.path('/timings');
          },
          onCreateAccountFailure: function (response){
            if (response.status === 400){
              angular.forEach(response.data, function(error, field){
                $scope.signupForm[field].$setValidity('', false);
              });
            }
          }
        });
      }
  ]);

  app.controller('LoginController',
    ['$scope', '$location', 'AccountFactory',
      function ($scope, $location, AccountFactory){
        $scope.accountFactory = new AccountFactory({
          onPerformLoginSuccess: function (response){
            $location.path('/timings');
          },
          onPerformLoginFailure: function (response){
            $scope.loginFailure = true;
          }
        });
      }
  ]);
})();

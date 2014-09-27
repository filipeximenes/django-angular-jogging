(function (){
  var app = angular.module('Jogging.accounts.ctrl', []);

  app.controller('AccountController',
    ['$scope', 'AccountFactory',
      function ($scope, AccountFactory){
        var accountFactoryCallbacks = {};
        accountFactoryCallbacks.createAccountCallback = function(data){

        };

        $scope.accountFactory = new AccountFactory(accountFactoryCallbacks);
      }
  ]);
})();

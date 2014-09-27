(function (){
  var app = angular.module('Jogging.accounts.service', []);

  app.factory('AccountFactory',
    ['Restangular',
      function (Restangular){
        var Factory = function(callbacks){
          this.createAccount = function (data){
            return Restangular.all('account').post(data).then(function (data){
              if (callbacks.createAccountCallback){
                return callbacks.createAccountCallback(data);
              }
              return data;
            });
          };
        };

        return Factory;
      }
  ]);
})();
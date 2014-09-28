(function (){
  var app = angular.module('Jogging.accounts.service', []);

  app.factory('AccountFactory',
    ['Restangular',
      function (Restangular){
        var Factory = function(callbacks){
          this.createAccount = function (data){
            return Restangular.all('accounts').post(data)
              .then(function (response){
                Restangular.setDefaultHeaders({Authorization: 'Token ' + response.data.token});
                if (callbacks.createAccountCallback){
                  return callbacks.createAccountCallback(response);
                }
              }, function (response){
                if (callbacks.createAccountCallback){
                  return callbacks.createAccountCallback(response);
                }
              });
          };
        };

        return Factory;
      }
  ]);
})();

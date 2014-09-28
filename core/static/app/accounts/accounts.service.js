(function (){
  var app = angular.module('Jogging.accounts.service', []);

  app.factory('AccountFactory',
    ['Restangular', '$cookies',
      function (Restangular, $cookies){
        var Factory = function(callbacks){
          var _this = this;

          this.createAccount = function (data){
            return Restangular.all('accounts').post(data)
              .then(function (response){
                _this.setCredentials(response.data.token);
                if (callbacks.createAccountCallback){
                  return callbacks.createAccountCallback(response);
                }
              }, function (response){
                if (callbacks.createAccountCallback){
                  return callbacks.createAccountCallback(response);
                }
              });
          };

          this.setCredentials = function (token){
            Restangular.setDefaultHeaders({Authorization: 'Token ' + token});
            $cookies.auth_token = token;
          };
        };

        return Factory;
      }
  ]);
})();

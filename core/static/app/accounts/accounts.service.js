(function (){
  var app = angular.module('Jogging.accounts.service', []);

  app.factory('AccountFactory',
    ['Restangular', '$cookies',
      function (Restangular, $cookies){
        var Factory = function(events){
          var _this = this;

          this.createAccount = function (data){
            return Restangular.all('accounts').post(data)
              .then(function (response){
                _this.setCredentials(response.data.token);
                if (events.onCreateAccountSuccess){
                  return events.onCreateAccountSuccess(response);
                }
              }, function (response){
                if (events.onCreateAccountFailure){
                  return events.onCreateAccountFailure(response);
                }
              });
          };

          this.performLogin = function (data){
            Restangular.all('login').post(data)
              .then(function (response){
                _this.setCredentials(response.data.token);
                if (events.onPerformLoginSuccess){
                  return events.onPerformLoginSuccess(response);
                }
              }, function (response){
                if (events.onPerformLoginFailure){
                  return events.onPerformLoginFailure(response);
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

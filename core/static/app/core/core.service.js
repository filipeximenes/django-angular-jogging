(function (){
  var app = angular.module('Jogging.core.service', []);

  app.factory('CoreFactory',
    ['Restangular', '$cookieStore',
      function (Restangular, $cookieStore){
        var obj = {};

        obj.logout = function (token){
          Restangular.setDefaultHeaders({Authorization: undefined});
          $cookieStore.remove('auth_token');
        };

        return obj;
      }
  ]);
})();

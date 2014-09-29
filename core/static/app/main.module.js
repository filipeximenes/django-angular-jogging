(function (){
  var app = angular.module('Jogging', [
                            'ngRoute',
                            'ngCookies',
                            'restangular',

                            'Jogging.core',
                            'Jogging.accounts',
                            'Jogging.timings']);

  app.config(
    ['$routeProvider',
      function ($routeProvider){
        $routeProvider.
          when('/', {
            templateUrl: 'login.html',
            controller: 'LoginController'
          }).
          when('/signup', {
            templateUrl: 'signup.html',
            controller: 'AccountCreateController'
          }).
          when('/timings', {
            templateUrl: 'timings.html',
            controller: 'TimingsCtrl'
          });
      }
  ]);

  app.config(
    ['$httpProvider', 'RestangularProvider',
      function ($httpProvider, RestangularProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.withCredentials = true;

        RestangularProvider.setBaseUrl('/api');
        RestangularProvider.setRequestSuffix('/');
        RestangularProvider.setFullResponse(true);
      }
  ]);

  app.run(
    ['$cookies', '$location', 'Restangular',
      function ($cookies, $location, Restangular){
        if ($cookies.auth_token){
          Restangular.setDefaultHeaders({Authorization: 'Token ' + $cookies.auth_token});
        }else{
          $location.path('/');
        }
      }
  ]);

})();

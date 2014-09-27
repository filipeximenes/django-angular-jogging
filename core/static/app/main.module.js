(function (){
  var app = angular.module('Jogging',
                          ['ngRoute',
                           'restangular',

                          'Jogging.accounts',
                          'Jogging.timings']);

  app.config(
    ['$routeProvider',
      function ($routeProvider){
        $routeProvider.
          when('/', {
            templateUrl: 'index.html',
            controller: 'AccountController'
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
      }
    ]);
})();

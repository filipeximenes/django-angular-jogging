(function (){
  var app = angular.module('Jogging',
                          ['ngRoute',

                          'Jogging.timings',]);

  app.config(
    ['$routeProvider',
      function ($routeProvider){
        $routeProvider.
          when('/', {
            templateUrl: 'timings.html',
            controller: 'TimingsCtrl'
          });
      }
  ]);
})();

(function (){
  var app = angular.module('Jogging.timings.ctrl', []);

  app.controller('TimingsCtrl',
    ['$scope', 'TimingsFactory',
      function ($scope, TimingsFactory){
        $scope.timings = TimingsFactory.timings;
      }
    ]);
})();

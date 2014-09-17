(function (){
  var app = angular.module('Jogging.timings.ctrl',
                          []);

  app.controller('TimingsCtrl',
    ['$scope',
      function ($scope){
        $scope.timings = [
          {
            date: '',
            distance: 100,
            time: 200,
          },
          {
            date: '',
            distance: 100,
            time: 200,
          }
        ];
      }
    ]);
})();

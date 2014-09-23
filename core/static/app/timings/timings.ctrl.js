(function (){
  var app = angular.module('Jogging.timings.ctrl', []);

  app.controller('TimingsCtrl',
    ['$scope', 'TimingsFactory', 'ConversionFactory',
      function ($scope, TimingsFactory, ConversionFactory){
        $scope.timingsFactory = TimingsFactory;
        $scope.conversionFactory = ConversionFactory;
      }
    ]);
})();

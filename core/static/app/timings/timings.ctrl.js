(function (){
  var app = angular.module('Jogging.timings.ctrl', []);

  app.controller('TimingsCtrl',
    ['$scope', 'TimingsFactory', 'ConversionFactory', 'ReportsFactory',
      function ($scope, TimingsFactory, ConversionFactory, ReportsFactory){
        $scope.timingsFactory = TimingsFactory;
        $scope.conversionFactory = ConversionFactory;
        $scope.reportsFactory = ReportsFactory;

        $scope.$watchCollection('timingsFactory.timings', function (){
          $scope.reportsFactory.byWeekFiltering($scope.timingsFactory.timings);
        });
      }
    ]);
})();

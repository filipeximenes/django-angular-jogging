(function (){
  var app = angular.module('Jogging.core.ctrl', []);

  app.controller('CoreController',
    ['$scope', 'CoreFactory',
      function ($scope, CoreFactory){
        $scope.coreFactory = CoreFactory;
      }
  ]);
})();

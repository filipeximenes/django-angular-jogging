(function (){
  var app = angular.module('Jogging.timings.service', []);

  app.factory('TimingsFactory',
    [
      function (){
        var timings = [
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

        var updateTimingList = function (){

        };

        var createTiming = function (){

        };

        var updateTiming = function (id){

        };

        var deleteTiming = function (id){

        };

        return {
          timings: timings,
          updateTimingList: updateTimingList,
          createTiming: createTiming,
          updateTiming: updateTiming,
          deleteTiming: deleteTiming,
        };
      }
    ]);
})();

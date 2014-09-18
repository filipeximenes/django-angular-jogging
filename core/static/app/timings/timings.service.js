(function (){
  var app = angular.module('Jogging.timings.service', []);

  app.factory('TimingsFactory',
    [
      function (){
        obj = {};
        obj.timings = [];

        obj.updateTimingList = function (){
          obj.timings = [
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
        };

        obj.createTiming = function (data){
          obj.timings.push(data);
        };

        obj.updateTiming = function (index, data){


        };

        obj.deleteTiming = function (index){

        };

        return obj;
      }
    ]);
})();

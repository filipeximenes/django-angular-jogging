(function (){
  var app = angular.module('Jogging.timings.service', []);

  app.factory('TimingsFactory',
    ['Restangular',
      function (Restangular){
        var timings = Restangular.all('timings');

        obj = {};
        obj.timings = [];

        obj.updateTimingList = function (){
          return timings.getList().then(function(data) {
            obj.timings = data;
            return data;
          });
        };

        obj.createTiming = function (data){
          return timings.post(data).then(function (data){
            obj.timings.push(data);
            return data;
          });
        };

        obj.updateTiming = function (index, data){
          var timingResource = Restangular.one('timings', obj.timings[index].id);
          angular.extend(timingResource, data);

          return timingResource.put().then(function (data){
            angular.extend(obj.timings[index], data);
            return data;
          });
        };

        obj.deleteTiming = function (index){
          obj.timings.splice(index, 1);
        };

        return obj;
      }
    ]);
})();

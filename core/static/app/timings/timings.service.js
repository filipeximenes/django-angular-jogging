(function (){
  var app = angular.module('Jogging.timings.service', []);

  app.factory('TimingsFactory',
    ['Restangular',
      function (Restangular){
        var timings = Restangular.all('timings');

        obj = {};
        obj.timings = [];

        obj.getTimingList = function (filters){
          return timings.getList(filters).then(function(data) {
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
          var timingResource = Restangular.one('timings', obj.timings[index].id);

          timingResource.remove().then(function (data){
            obj.timings.splice(index, 1);
            return data;
          });
        };

        return obj;
      }
    ]);

  app.factory('ConversionFactory',
    [
      function (){
        var obj = {};

        obj.from_seconds_to_formated = function (total_secs){
          var hours = '' + Math.floor(total_secs / 3600);
          var minutes = '' + Math.floor((total_secs % 3600) / 60);
          var seconds = '' + ((total_secs % 3600) % 60);

          if (hours.length === 1){
            hours = '0' + hours;
          }

          if (minutes.length === 1){
            minutes = '0' + minutes;
          }

          if (seconds.length === 1){
            seconds = '0' + seconds;
          }

          return hours + ':' + minutes + ':' + seconds;
        };

        obj.from_formated_to_seconds = function (formated){
          if (!formated){
            return 0;
          }

          var splits = formated.split(':');

          var seconds = parseInt(splits.pop(), 10) || 0;
          var minutes = parseInt(splits.pop(), 10) || 0;
          var hours = parseInt(splits.pop(), 10) || 0;

          return (hours * 3600) + (minutes * 60) + seconds;
        };

        return obj;
      }
    ]);
})();

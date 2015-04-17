(function (){
  var app = angular.module('Jogging.timings.service', []);

  app.factory('TimingsFactory',
    ['Restangular', 'ConversionFactory',
      function (Restangular, ConversionFactory){
        var timingsResource = Restangular.all('timings');

        obj = {};
        obj.timings = [];

        obj.getTimingList = function (filters){
          return timingsResource.getList(filters).then(function (response){
            obj.timings = response.data;
          });
        };

        obj.createTiming = function (data){
          data.time = ConversionFactory.fromFormattedToSeconds(createData.formattedTime);

          return timingsResource.post(data).then(function (response){
            obj.timings.push(response.data);
          });
        };

        obj.updateTiming = function (index, data){
          var timingResource = Restangular.one('timings', obj.timings[index].id);
          angular.extend(timingResource, data);

          return timingResource.put().then(function (response){
            angular.extend(obj.timings[index], response.data);
          });
        };

        obj.deleteTiming = function (index){
          var timingResource = Restangular.one('timings', obj.timings[index].id);

          timingResource.remove().then(function (response){
            obj.timings.splice(index, 1);
          });
        };

        return obj;
      }
    ]);

  app.factory('ConversionFactory',
    [
      function (){
        var obj = {};

        obj.fromSecondsToFormatted = function (total_secs){
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

        obj.fromFormattedToSeconds = function (formatted){
          if (!formatted){
            return 0;
          }

          var splits = formatted.split(':');

          var seconds = parseInt(splits.pop(), 10) || 0;
          var minutes = parseInt(splits.pop(), 10) || 0;
          var hours = parseInt(splits.pop(), 10) || 0;

          return (hours * 3600) + (minutes * 60) + seconds;
        };

        return obj;
      }
    ]);

  app.factory('ReportsFactory',
    [
      function (){
        var obj = {};

        obj.report = {};

        obj.byWeekFiltering = function (timings){
          obj.report = {};
          angular.forEach(timings, function (timing){
            var date = moment(timing.date);
            if (!obj.report[date.weeks()]){
              obj.report[date.weeks()] = [];
            }

            obj.report[date.weeks()].push(timing);
          });

          return obj.report;
        };

        obj.calculateTotalDistance = function (timings){
          var total = 0;
          angular.forEach(timings, function (timing){
            total += timing.distance;
          });
          return total;
        };

        obj.calculateAverageSpeed = function (timings){
          var totalDistance = 0;
          var totalTime = 0;
          angular.forEach(timings, function (timing){
            totalDistance += timing.distance;
            totalTime += timing.time;
          });
          return totalDistance / totalTime;
        };

        return obj;
      }
    ]);
})();

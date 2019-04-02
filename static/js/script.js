(function() {
    "use strict";

    //  JS for homepage
    var app = angular.module("myApp", []);

    app.controller("myCntrl", function($scope, $http, $window) {
        // $scope.getRequest = function() {
        console.log("Controller started");
        $http.get("/getmedicines").then(
            function successCallBack(response) {
                $scope.obj = response.data;
                console.log("response received!");
            },
            function errorCallBack(response) {
                console.log("Unable to perform request");
            }
        );

        $scope.getDrugData = function(id) {
            var url = '/getDrugData?id=' + id;
            // use ng-view and not reload the page
            $window.location.href = url;
        };
    });

    // JS for homepage ends

    // JS for medicinePage starts

    var medicineApp = angular.module('medicineApp', ['ui-bootstrap']);

    medicineApp.controller("CarouselCtrl", ['$scope', '$rootScope', function($scope, $rootScope) {
        console.log("inside controller");

        $scope.myInterval = 2000;
        $scope.slides = [{
            image: 'https://www.practostatic.com/practopedia-images/res-150/0f2933bef3610b4f478d56e34d288c0892269b461.jpg',
            id: 2
        }, {
            image: 'https://www.practostatic.com/practopedia-images/res-150/a059a5ae1816712e9b88da3ddfd18aaf36d9c96e6.JPG',
            id: 22
        }, {
            image: 'https://www.practostatic.com/practopedia-images/res-master/1877d81414ce213efaf38b99ba7622c608dabe271_cropped_not_compressed.JPG',
            id: 222
        }, ];
        // $scope.name=$rootScope.obj[0]["type"];
    }]);

    // JS for medicinePage ends
})(angular, $)


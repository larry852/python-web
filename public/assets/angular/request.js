var app = angular.module("mainModule", []);

app.controller("controller",function($scope,$http){

	$scope.search = function(){
		params = {url: $scope.url, word: $scope.word};
		$http.post("search?"+$scope.url+"?"+$scope.word, params)
		.success(function(data){
			$scope.active = true;
			if(data == 'si')
				$scope.answer = true;
			else
				$scope.answer = false;
		})
		.error(function(err){
			alert('Error en el servidor. Contacte con el administrador.');
		})
	}
});
app.controller("myctrl",($scope,$window,$localStorage,myfactory)=>{
    $scope.call=(userid,pass)=>{
        var promise=myfactory.calldata(userid,pass);
        promise.then( function(data){
            console.log(data.data);
          data.data.filter((arr)=>{
                if(arr.username==userid && arr.pass==pass){
                   $scope.store= $localStorage;
                    $scope.store.email=userid;
                    $scope.store.name=arr.name;
                    $scope.store.address=arr.address;
                      $scope.store.url=arr.url;
                    $window.open("welcome.html","_target");
                }
            }) ;  
        },function(err){
            $scope.result= err;
        });        
        
    }
        $scope.submit=function(isValid){
				if(isValid){
               console.log("Form Submit");
				}
				else{
					alert("Form is Not Valid so Can't Submit");
				}
            }
});
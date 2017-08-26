app2.controller("myctrl2",($scope,$localStorage,$window,myfactory2)=>{
    $scope.store2=$localStorage;
    $scope.name=$scope.store2.name;
    $scope.email=$scope.store2.email;
    $scope.address=$scope.store2.address;
    $scope.url=$scope.store2.url;
    $scope.quesobj;
    $scope.sno=1;
    $scope.mark=false;
     $scope.green=false;
   $scope.load=function(){
        var promise=myfactory2.calldata();
        promise.then(function(data){
            $scope.quesobj=data.data;
            console.log(data);
            console.log("hello"+data.id)
        },function(err){
            console.log("error is"+err);})
    };
    $scope.close=()=>{
        $window.close("welcome.html","index.html");
    }
    $scope.showAnswer=(radio,i)=>{
        $scope.answer=myfactory2.checkans(radio,i);
    }
    $scope.mark=(i,radio)=>{
        if($scope.radio!=""){
            return i.mark=true;
        }
        return i.mark;
    }
    $scope.next=(i)=>{
        $scope.answer="";
         if($scope.radio=""){
           $scope.green=true; 
        }
        $scope.sno++;
        if($scope.sno>$scope.quesobj.length){
            $scope.sno=1;
        }
        
    }
     $scope.previous=()=>{
          $scope.answer="";
        $scope.sno--;
         if($scope.sno<1){
            $scope.sno=1;
        }
    }
})
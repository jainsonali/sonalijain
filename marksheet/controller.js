app.controller("myctrl",($scope,myfactory)=>{
    $scope.compute_total=()=>{
                  $scope.total=myfactory.total($scope.sub1,$scope.sub2,$scope.sub3,$scope.sub4,$scope.sub5);
                $scope.subarray=myfactory.subject($scope.sub1,$scope.sub2,$scope.sub3,$scope.sub4,$scope.sub5);
            $scope.subjectarray=myfactory.getsubjectarray();
        console.log($scope.subjectarray);
        }
     $scope.compute_percent=()=>{
                  $scope.percentage=myfactory.percentage($scope.total);
     }
    $scope.compute_grade=()=>{
                 $scope.grade=myfactory.grade($scope.percentage);
    }
    $scope.id=1;
    $scope.add=()=>{
        $scope.call=myfactory.data($scope.id,$scope.name,$scope.rollno,$scope.class,$scope.subjectarray,$scope.total,$scope.percentage,$scope.grade);
        $scope.dataarray=myfactory.getdata();
        console.log($scope.dataarray);
        $scope.id++;
    }
   
});
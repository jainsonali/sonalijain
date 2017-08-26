app2.factory("myfactory2",($http,$q)=>{
    var object={
        calldata(){
             var pr=$q.defer();
            var url="question.JSON";
            $http.get(url).then(function(data){
                console.log(data);
                pr.resolve(data);
                },function(err){
                console.log(err);
					pr.reject(err);
				});
				return pr.promise;
			},
        checkans(radio,i){
            if(radio==""){
                return  "Answer is "+i.ans;
            }
            else if(radio==i.ans){
                return "correct answer";
            }
            else{
                return "wrong answer. Answer is "+i.ans;
            }
        }
    }
    return object;
});
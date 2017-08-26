app.factory("myfactory",($http,$q)=>{
    var object={
        calldata(username,pass){
            var pr=$q.defer();
            var url="login.JSON";
            $http.get(url).then(function(data){
                console.log(data);
                pr.resolve(data);
                },function(err){
                console.log(err);
					pr.reject(err);
				});
				return pr.promise;
			}
        }
    return object;
});
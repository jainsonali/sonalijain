app.factory("myfactory",()=>{
    var object={
        data_array:[],
        subjectarray:[],
        total(sub1,sub2,sub3,sub4,sub5){
        var sum=0;
        sum = parseInt(sub1)+parseInt(sub2)+parseInt(sub3)+parseInt(sub4)+parseInt(sub5);
        return sum;
        },
        percentage(add){
            var percentage= add/5;
            return percentage;  
        },
        grade(percent){
            if(percent>=90){
                return "GradeA";
            }
            else if(90>percent>=80){
                return "GradeB";
            }
            else
                return "GradeC";
        },
        subject(s1,s2,s3,s4,s5){
          var obj={
              subject1:s1,
              subject2:s2,
              subject3:s3,
              subject4:s4,
              subject5:s5
              
          };
            this.addsubarray(obj);
        },
        addsubarray(obj){
            this.subjectarray.push(obj);
        },
        getsubjectarray(){
             return subjectarray;
        },
        data(sno,name,rollno,classname,array,total,percent,grade){
            var obj2={
                id:sno,
                Name:name,
                Rollno:rollno,
                Class:classname,
                marks:array,
                total:total,
                percentage:percent,
                Grade:grade
            };
            this.adddata(obj2);
            return obj2;
        },
        adddata(obj2){
            this.data_array.push(obj2);
            
        },
        getdata(){
            return this.data_array;
        }
    }
            return object;
    
});
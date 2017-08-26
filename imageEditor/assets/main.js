

$(document).ready(function(){
    var effect;
    var file_name;
    $("#file").change(function(){
        file_name = document.getElementById("file").files[0].name;
        $("#image").attr('src',"assets/images/"+file_name)
    })
    $(".effects").click(function(){
        effect = $(this).html();
        $("#range").css("display","block");
    })
    $("#range").change(function(){
        var range_value = $(this).val();
        if(effect=="brightness"||"contrast"||"grayscale"||"invert"||"opacity"||"sepia"||"saturate"){
            $("#image").css("-webkit-filter",effect.toLocaleLowerCase()+'('+range_value+"%"+')');
        }
       if(effect=="blur"){
         $("#image").css("-webkit-filter",effect.toLocaleLowerCase()+'('+parseInt(range_value)+"px"+')');
        }
        else if(effect=="none")
        {
           $("#image").css("-webkit-filter",effect.toLocaleLowerCase());
        }
    })
    })

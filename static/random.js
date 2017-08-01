    

    $(function () {
    var run = 0,
        heading = $("#eat_tip"),
        timer;

    var dic , list = new Array() ,parms= new Array() ;
    $.get('./get_data',{'media_id':getUrlParam('media_id')},
    function(data,status,xhr){
        dic = data;
    },"json");
    


    $("#start").click(function () {
        $("#detail").hide();
        if (!run) {
            heading.html("努力选择ing");
            $(this).html("停止");
            timer = setInterval(function () {
                var r = Math.ceil(Math.random() * list.length),
                    food = list[r - 1];
                $("#eat_result").html(food);
                var rTop = Math.ceil(Math.random() * $(document).height()-30),
                    rLeft = Math.ceil(Math.random() * ($(document).width() - 50)),
                    rSize = Math.ceil(Math.random() * (20 - 14) + 14);
                $("<span class='temp' ></span>").html(food).hide().css({
                    "top": rTop,
                    "left": rLeft,
                    "color": "rgba(0,0,0,." + Math.random() + ")",
                    "fontSize": rSize + "px"
                }).appendTo("body").fadeIn("slow", function () {
                    $(this).fadeOut("slow", function () {
                        $(this).remove();
                    });
                });
            }, 50);
            run = 1;
        } else {
            heading.html("吃这个");
            $(this).html("换一个");
            $("#detail").show();
            clearInterval(timer);
            run = 0;
        };
    });


    $('.eat_how').click(function(){
        $('#first_page').fadeOut('fast',function(){
            $('#second_page').fadeIn('fast');
        });
        parms.push($(this).attr('id'));
    })
    $('.eat_where').click(function(){
        $('#second_page').fadeOut('fast',function(){
            $('#third_page').fadeIn('fast');
        });
        parms.push($(this).attr('id'));
        for(i in dic){
            if(dic[i][parms[0]] == 1 && dic[i][parms[1]] == 1){
                list.push(dic[i]['name']);
            }
        }
    })

});

function getUrlParam(name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
            var r = window.location.search.substr(1).match(reg);  //匹配目标参数
            if (r != null) return unescape(r[2]); return null; //返回参数值
        }
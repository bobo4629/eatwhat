    $(function () {
    var run = 0,
        heading = $("#eat-tip"),
        timer;

    $("#start").click(function () {
        var list = $("#list").val().replace(/ +/g, " ").replace(/^ | $/g, "").split(" ");
        $("#detail").hide();
        if (!run) {
            heading.html("努力选择ing");
            $(this).html("停止");
            timer = setInterval(function () {
                var r = Math.ceil(Math.random() * list.length),
                    food = list[r - 1];
                $("#eat-result").html(food);
                var rTop = Math.ceil(Math.random() * $(document).height()-30),
                    rLeft = Math.ceil(Math.random() * ($(document).width() - 50)),
                    rSize = Math.ceil(Math.random() * (20 - 14) + 14);
                $("<span class='temp' style='positive:absolute'></span>").html(food).hide().css({
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

});
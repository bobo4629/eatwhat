
$(function(){
    reset();

    $("#reset").click(function(){
        reset();
    })

    $('#add').click(function(){
        $.post('./set_data',
        {
            'name':$('#name').val(),
            'eat_here':$('#eat_here').val(),
            'eat_out':$('#eat_out').val(),
            'area_1':$('#area_1').val(),
            'area_2':$('#area_2').val(),
            'area_3':$('#area_3').val(),
            'area_4':$('#area_4').val(),
            'id':$('#media_id').html()
        },
        function(data){
            if(data == 'done')
                alert("成功")
        }
        )
    })

    $('#delete').click(function(){
         $.post('./delete_data',
        {
            'name':$('#name').val(),
        },
        function(data){
            if(data == 'done')
                alert("成功")
        }
        )
    })
})

function reset(){
    $(".input-form-50").val("1");
    $('.input-form').val('');
}

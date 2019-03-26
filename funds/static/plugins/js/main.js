$(function() {
    $('#select').change(function(){
        $('.option').hide();
        $('#' + $(this).val()).show();
    });
    $('#select1').change(function(){
        $('.option1').hide();
        $('#' + $(this).val()).show();
    });
    $('#select2').change(function(){
        $('.option2').hide();
        $('#' + $(this).val()).show();
    });
    $('#select3').change(function(){
        $('.option3').hide();
        $('#' + $(this).val()).show();
    });
    $('#select4').change(function(){
        $('.option4').hide();
        $('#' + $(this).val()).show();
    });
});

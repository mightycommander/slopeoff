$(document).ready(function(){
    $(".scroller").click(function() {
        $('html, body').animate({
            scrollTop: $("#formContainer").offset().top
        }, 1000);
    });
});

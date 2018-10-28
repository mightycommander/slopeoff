$(document).ready(function(){
    $(".scroller").click(function() {
        $('html, body').animate({
            scrollTop: $(".break").offset().top + (100)
        }, 1000);
    });
});

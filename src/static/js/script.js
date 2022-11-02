$(document).ready(function() {
    $(".link").click(function () {
        $(".link").removeClass("active");
        // $(".tab").addClass("active"); // instead of this do the below 
        $(this).addClass("active");   
    });
});





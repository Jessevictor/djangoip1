$(function () {
    var selectedClass = "";
    $(".filter").click(function () {
        selectedClass = $(this).attr("data-rel");
        $("#gallery").fadeTo(100, 0.1);
        $("#gallery div").not("." + selectedClass).fadeOut().removeClass('animation');
        setTimeout(function () {
            $("." + selectedClass).fadeIn().addClass('animation');
            $("#gallery").fadeTo(300, 1);
        }, 300);
    });
});

function myFunction() {
 
    var copyText = document.getElementById("myInput");
    copyText.select();
    copyText.setSelectionRange(0, 99999); 
  
    document.execCommand("copy");
  
    alert("Copied the text: " + copyText.value);
  }
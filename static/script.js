var upload = function(){
    var image = $('#input')[0].files[0];
    formdata = new FormData();
    formdata.append( 'image', image );
    formdata.append( 'action', 'save-image' );

    $(".flex1").html("<img id='wait' src='static/media/giphy.gif' alt='output' /><p<Please Wait</p>")

    

    $.ajax({
        url: '/upload',
        type: 'POST',
        data: formdata,
        processData: false,
        contentType: false,
        success: function( res ) {
            console.log(res)
            $(".flex1").html(
    
                "<a href='" + res +  "' download ><img id='output' src='" + res + "' alt='output'></a>"+
                "<p>Click On Image To Download</p>"+
                "<div class='button' id='reupload'>upload" +
                "<input type='file' id='input' class='input' name='image' accept='Image/*' onchange='upload()'> "+
                "</div>"
            )
        },
        error : function(err) {
            console.log("Erorrrr")
        }
    });
}


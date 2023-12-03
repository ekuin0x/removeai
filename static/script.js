$("input").change(async function(){
    let file = $("input").prop("files")[0]
    $("#drop").html("<img src='/static/media/giphy.gif' />")
    $("#drop").css("background-color", "transparent")
    var data = new FormData()
    data.append('file', file)
    let res = await fetch("/data", {
        method : 'post',
        body : data
    })
    url = await res.text()
    $("#drop").html(`<img src='${url}' />`)
    $(".button").css("display", "block")
    $("#save").attr("href", url)    
})
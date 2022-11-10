$(document).ready(function () {

    console.log("erwre")
});


$(".submit-btn").on('click', function (e) {
    var myFile = $('.input-psd-file').prop('files');
    var numMerge = $('.input-num-merge').val();
    var mergeCondition = $('#merge-condition').val();
    var counter = $('.input-counter').val();
    console.log(myFile)

    var form = new FormData();
    form.append("file", myFile[0]);
    form.append("num_merge", numMerge);
    form.append("merge_condition", mergeCondition);
    form.append("counter", counter);

    var settings = {
        "url": "http://127.0.0.1:8000/psd/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });

});

$(".input-psd-file").on('input', function (e) {
    var fileName = e.target.files[0].name;
    $(".psd-input-title").html(fileName)
});

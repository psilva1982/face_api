$(document).ready(() => {
    $("#loading").hide();
    const submitedImage = $("#submitedFile").val()
    if (submitedImage) {
        const host = $(location).attr('origin')
        const imgPath = `${host}/media/${submitedImage}`
        $("#imgPreview").attr("src", imgPath);
    } else {
        $(".holder").hide();
    }

    $("#id_photo").change(function () {
        const file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $("#imgPreview")
                  .attr("src", event.target.result);
            };
            reader.readAsDataURL(file);
            $(".holder").show();
        }
    });

    $("#search-face-form").submit(function() {
        $("#search-face-button").val("Pesquisando...");
        $("#loading").fadeIn();
    });
});

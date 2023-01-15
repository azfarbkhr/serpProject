$(document).ready(function () {
    var consultation_add_url = $('#consultation_add_url')[0].href;
    $('.top').prepend('<a href="' + consultation_add_url + '"><button class="btn btn-primary" id="addConsultation" style="margin-left: 3px;"><i class="fas fa-plus"></i></button>');
    
});
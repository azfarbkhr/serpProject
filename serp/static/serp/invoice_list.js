$(document).ready(function () {
    var invoice_add_url = $('#invoice_add_url')[0].href;
    $('.top').prepend('<a href="' + invoice_add_url + '"><button class="btn btn-primary" id="addInvoice" style="margin-left: 3px;"><i class="fas fa-plus"></i></button>');
    
});
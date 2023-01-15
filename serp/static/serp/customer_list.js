$(document).ready(function () {
    var customer_add_url = $('#customer_add_url')[0].href;
    $('.top').prepend('<a href="' + customer_add_url + '"><button class="btn btn-primary" id="addCustomer" style="margin-left: 3px;"><i class="fas fa-plus"></i></button>');
    
});
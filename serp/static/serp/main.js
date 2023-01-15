function loadDataTables() {
    $.fn.dataTable.moment('MMM. D, YYYY');

    $('.myDataTable').DataTable({
        lengthMenu: [
            [25, 50, 200, -1],
            [25, 50, 200, 'All'],
        ],
        "iDisplayLength": 25,
        "scrollX": true,
        deferRender: true,
        orderClasses: false,
        order : [],
        select: {
            style: 'multi',
            selector: 'td:first-child'
        },
        columnDefs: [
            {
                'targets': 0,
                'checkboxes': {
                   'selectRow': true
                }
             }
        ],
        colReorder: {
            realtime: false
        },
        buttons: [
            {
                extend: 'excelHtml5',
                text: '<i class="fas fa-file-excel"></i>',
            }, 
            {
                extend: 'colvis',
                text: '<i class="fas fa-columns"></i>  ',
            },
        ],
        dom: '<"top"Bf>rt<"bottom"lp><"clear">',
    });

    $('button').removeClass('dt-button');
    $('button').addClass('btn btn-primary');
    $('button.buttons-colvis').html('<i class="fas fa-columns"></i>  ');
            
    $('.hidden').removeClass('hidden');
    $('.myDataTable').DataTable().columns.adjust().draw();
    
};




$(document).ready(function () {
    loadDataTables();    
});

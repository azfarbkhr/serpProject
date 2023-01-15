function loadDataTables() {
    $.fn.dataTable.moment( 'MMM. D, YYYY');

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
    
    $('.top').prepend('<button class="btn btn-primary" id="bulkEditButton"><i class="fas fa-edit"></i></button>');
    $('#bulkEditButton').css('margin-left', '3px');

    $('#bulkEditButton').click(function () {
        // show a modal to edit the selected rows
        $('#bulkEditModal').modal('show');
    });

    // // on save button click from the modal send data for the selected rows
    // $('#saveButton').click(function () {
    //     // get the selected rows
    //     var rows_selected = $('.myDataTable').DataTable().column(0).checkboxes.selected();
    //     console.log(rows_selected);
    // });
        
    $('.hidden').removeClass('hidden');
    $('.myDataTable').DataTable().columns.adjust().draw();
    
};




$(document).ready(function () {
    loadDataTables();
    
});

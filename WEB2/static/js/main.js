$(document).ready(function () {
    $('#dataTable').DataTable(
        {
            drawCallback: function(){
                $("img.lazy").lazyload();
            }
        }
    /*    {"columns": [
        { "width": "10%" },
        { "width": "10%" },
        null,
        { "width": "20%" },
      ]
    }*/
    );
    $('[data-table]').each(function(){
        $(this).DataTable({
            drawCallback: function(){
                $("img.lazy").lazyload();
            }
        });
    });
});

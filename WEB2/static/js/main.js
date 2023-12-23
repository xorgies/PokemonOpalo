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
});

/*
 *  Document   : ecomOrders.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in eCommerce Orders page
 */

var EcomOrders = function() {

    return {
        init: function() {
            /* Extend with date sort plugin */
            $.extend($.fn.dataTableExt.oSort, {
                "date-custom-pre": function ( a ) {
                    var customDate = a.split('/');
                    return (customDate[2] + customDate[1] + customDate[0]) * 1;
                },

                "date-custom-asc": function ( a, b ) {
                    return ((a < b) ? -1 : ((a > b) ? 1 : 0));
                },

                "date-custom-desc": function ( a, b ) {
                    return ((a < b) ? 1 : ((a > b) ? -1 : 0));
                }
            } );

            /* Initialize Bootstrap Datatables Integration */
            App.datatables();

            /* Initialize Datatables */
            $('#ecom-orders').dataTable({
                columnDefs: [
                    { type: 'date-custom', targets: [6] },
                    { orderable: false, targets: [7] }
                ],
                order: [[ 0, "desc" ]],
                pageLength: 20,
                lengthMenu: [[10, 20, 30, -1], [10, 20, 30, 'All']]
            });

            /* Add placeholder attribute to the search input */
            $('.dataTables_filter input').attr('placeholder', 'Search');
        }
    };
}();
/*
 *  Document   : readyFiles.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Files page
 */

var ReadyFiles = function() {

    return {
        init: function() {
            var mediaFilter = $('.media-filter');
            var mediaItems  = $('.media-filter-items');
            var showCategory;

            // When a media filter link is clicked
            mediaFilter.find('a').on('click', function() {
                // Get its data-category value
                showCategory = $(this).data('category');

                // Procceed only if the user clicked on an inactive category
                if ( ! $(this).parent().hasClass('active')) {
                    // Remove active class from all filter links
                    mediaFilter.find('a').parent().removeClass('active');

                    // Add the active class to the clicked link
                    $(this).parent().addClass('active');

                    // If the value is 'all' hide the current visible items and show them all together, else hide them all and show only from the category we need
                    if (showCategory === 'all') {
                        mediaItems
                            .find('.media-items')
                            .parent()
                            .hide(0, function(){
                                $(this).show(0);
                            });
                    } else {
                        mediaItems
                            .find('.media-items')
                            .parent()
                            .hide(0, function(){
                                mediaItems
                                    .find('[data-category="' + showCategory + '"]')
                                    .parent('div')
                                    .show(0);
                            });
                    }
                }
            });
        }
    };
}();

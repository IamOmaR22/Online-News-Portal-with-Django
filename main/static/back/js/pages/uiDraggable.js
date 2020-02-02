/*
 *  Document   : uiDraggable.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Draggable Blocks page
 */

var UiDraggable = function() {

    return {
        init: function() {
            /* Initialize draggable and sortable blocks, check out more examples at https://jqueryui.com/sortable/ */
            $('.draggable-blocks').sortable({
                connectWith: '.block',
                items: '.block',
                opacity: 0.75,
                handle: '.block-title',
                placeholder: 'draggable-placeholder',
                tolerance: 'pointer',
                start: function(e, ui){
                    ui.placeholder.css('height', ui.item.outerHeight());
                }
            });
        }
    };
}();
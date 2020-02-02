/*
 *  Document   : readyTickets.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Tickets page
 */

var ReadyTickets = function() {
    return {
        init: function() {
            // If a hash is added to the url page and belongs to a tab, show the tab
            var activeTab = $('[href="' + location.hash + '"]');
            activeTab && activeTab.tab('show');
        }
    };
}();

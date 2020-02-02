/*
 *  Document   : readyTasks.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Tasks page
 */

var ReadyTasks = function() {

    return {
        init: function() {
            var taskList        = $('.task-list');
            var taskInput       = $('#add-task');
            var taskInputVal    = '';

            /* On page load, check the checkbox if the class 'task-done' was added to a task */
            $('.task-done input:checkbox').prop('checked', true);

            /* Toggle task state */
            taskList.on('click', 'input:checkbox', function(){
                $(this).parents('li').toggleClass('task-done');
            });

            /* Remove a task from the list */
            taskList.on('click', '.task-close', function(){
                $(this).parents('li').slideUp();
            });

            /* Add a new task to the list */
            $('#add-task-form').on('submit', function(){
                // Get input value
                taskInputVal = taskInput.prop('value');

                // Check if the user entered something
                if ( taskInputVal ) {
                    // Add it to the task list
                    taskList
                        .prepend('<li class="animation-slideUp">' +
                            '<a href="javascript:void(0)" class="task-close"><i class="fa fa-times"></i></a>' +
                            '<label class="checkbox-inline">' +
                            '<input type="checkbox">' +
                            $('<span />').text(taskInputVal).html() +
                            '</label>' +
                            '</li>');

                    // Clear input field
                    taskInput.prop('value', '').focus();
                }

                // Don't let the form submit
                return false;
            });
        }
    };
}();

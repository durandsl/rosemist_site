function submitForm(frm, e) {
    e.preventDefault();

    // POST values in the background the the script URL
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        // data = JSON object that the action returns
        success: function(data) {
            // we recieve the type of the message: success x danger and apply it to the 
            var messageAlert = 'alert-' + data.type;
            var messageText = data.message;

            // let's compose Bootstrap alert box HTML
            var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' + messageText + '</div>';

            // If we have messageAlert and messageText
            if (messageAlert && messageText) {
                // inject the alert to .messages div in our form
                frm.find('.messages').html(alertBox);
                // empty the form
                frm[0].reset();
            }
        }
    });
    return false;
}

$(function() {
    // when the form is submitted
    $('#contact-form').submit(function(e) {
        submitForm($(this), e);
    })
});
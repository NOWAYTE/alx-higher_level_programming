//toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header

$('div#toggle_header').click(function() {
        var header = $('header');
        if (header.hasClass('red')) {
          header.removeClass('red').addClass('green');
        } else if (header.hasClass('green')) {
          header.removeClass('green').addClass('red');
        } else {
          header.addClass('red'); // Default to red if no class is present
        }

$(document).ready(function() {
    $('.portletRss .portletHeader a').replaceWith(function() {return $(this).contents();})
});

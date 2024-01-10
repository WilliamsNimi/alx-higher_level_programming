#!/usr/bin/node
const $ = window.$;
const toggleSelect = 'DIV#toggle_header';
$(toggleSelect).addClass('green');
$(toggleSelect).click(function () {
  if ($(toggleSelect).hasClass('green')) {
    $(toggleSelect).removeClass('green');
    $(toggleSelect).addClass('red');
  } else {
    $(toggleSelect).removeClass('red');
    $(toggleSelect).addClass('green');
  }
});

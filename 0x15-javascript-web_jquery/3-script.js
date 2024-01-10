#!/usr/bin/node
const $ = window.$;
const selectRed = 'DIV#red_header';
$(selectRed).click(function () {
  $(selectRed).addClass('red');
});

#!/usr/bin/node
const $ = window.$;
const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(URL, function (data, status) {
  $('DIV#hello').text(data.hello);
});

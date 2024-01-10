#!/usr/bin/node
const $ = window.$;
$(document).ready(
  function () {
    $('#btn_translate').click(function () {
      const input = $('INPUT#language_code')[0].value;
      const URL = `https://hellosalut.stefanbohacek.dev/?lang=${input}`;
	    $.get(URL, function (data, status) {
        $('DIV#hello').text(data.hello);
	    });
    });
  }
);

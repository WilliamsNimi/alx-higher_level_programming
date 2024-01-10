#!/usr/bin/node
const $ = window.$;
const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(URL, function (data, status) {
  $('DIV#character').text(data.name);
});

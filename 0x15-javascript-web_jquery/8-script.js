#!/usr/bin/node
const $ = window.$;
const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(URL, function (data, status) {
  for (const i of data.results) {
    $('UL#list_movies').append('<li>${i.title}</li>');
  }
});

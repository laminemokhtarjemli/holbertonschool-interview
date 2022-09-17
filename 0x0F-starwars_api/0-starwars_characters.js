#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
const charDict = {};

request(url, function (err, res, body) {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  characters.forEach((char) => {
    request(char, function (err, res, body) {
      if (err) console.log(err);
      const name = JSON.parse(body).name;
      charDict[char] = name;
      if (Object.values(charDict).length === characters.length) {
        characters.forEach((character) => {
          console.log(charDict[character]);
        });
      }
    });
  });
});

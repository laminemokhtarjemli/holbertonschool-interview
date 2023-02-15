#!/usr/bin/node
// characters of a Star Wars film
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    const names = [];

    for (let i = 0; i < characters.length; i++) {
      const res = await new Promise((resolve, reject) => {
        request(characters[i], (error, res, html) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      names[i] = res;
    }

    for (let i = 0; i < characters.length; i++) {
      console.log(names[i]);
    }
  }
});

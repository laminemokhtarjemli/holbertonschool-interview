#!/usr/bin/node
// characters of a Star Wars films
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (const characterUrl of characters) {
      const res = await new Promise((resolve, reject) => {
        request(characterUrl, (error, res, html) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});

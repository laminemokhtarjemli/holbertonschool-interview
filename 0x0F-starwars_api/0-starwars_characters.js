#!/usr/bin/node
const request = require('request');

async function getCharacterNames(urls, index = 0) {
  if (index >= urls.length) return;
  return new Promise((resolve, reject) => {
    request(urls[index], (err, res, body) => {
      if (!err) {
        const character = JSON.parse(body);
        console.log(character.name);
        resolve(getCharacterNames(urls, index + 1));
      } else {
        reject(err);
      }
    });
  });
}

(async () => {
  try {
    const movieData = await new Promise((resolve, reject) => {
      request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
        if (!err) {
          const movie = JSON.parse(body);
          if(movie.detail) {
            console.log(`Error: ${movie.detail}`);
            return;
          }
          resolve(movie);
        } else {
          reject(err);
        }
      });
    });
    await getCharacterNames(movieData.characters);
  } catch (err) {
    console.error(err);
  }
})();

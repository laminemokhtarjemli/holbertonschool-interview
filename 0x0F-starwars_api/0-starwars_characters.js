#!/usr/bin/node
const request = require('request');

async function getCharacterNames(urls, index = 0) {
  try {
    if (index >= urls.length) return;
    const characterData = await request({uri: urls[index], json: true});
    console.log(characterData.name);
    await getCharacterNames(urls, index + 1);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  try {
    const movieData = await request({uri: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, json: true});
    if(movieData.detail) {
      console.log(`Error: ${movieData.detail}`);
      return;
    }
    await getCharacterNames(movieData.characters);
  } catch (err) {
    console.error(err);
  }
})();

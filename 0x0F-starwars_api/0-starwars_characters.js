const request = require('request-promise-native');
const MovieID = process.argv[1];
const url = `https://swapi-api.hbtn.io/api/films/${MovieID}`;

async function getCharacterNames() {
  try {
    const movieData = await request({uri: url, json: true});
    if(movieData.detail) {
      console.log(`Error: ${movieData.detail}`);
      return;
    }
    const characters = movieData.characters;
    const characterPromises = characters.map(url => request({uri: url, json: true}));
    const characterData = await Promise.all(characterPromises);
    characterData.forEach(charData => {
      console.log(charData.name);
    });
  } catch (err) {
    console.error(err);
  }
}

getCharacterNames();

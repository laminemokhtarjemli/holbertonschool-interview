#!/usr/bin/node
const request = require('request');

function getCharacterNames(urls, index = 0) {
  request(urls[index], (err, res, body) => {
    if (!err) {
      const character = JSON.parse(body);
      console.log(character.name);
      if (index + 1 < urls.length) getCharacterNames(urls, index + 1);
    }
  });
}

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
  if (!err) {
    const movie = JSON.parse(body);
    if(movie.detail) {
      console.log(`Error: ${movie.detail}`);
      return;
    }
    getCharacterNames(movie.characters);
  }
});
#!/usr/bin/node
const request = require('request');

function getCharacterNames(urls, index = 0) {
  request(urls[index], (err, res, body) => {
    if (!err) {
      const character = JSON.parse(body);
      console.log(character.name);
      if (index + 1 < urls.length) getCharacterNames(urls, index + 1);
    }
  });
}

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
  if (!err) {
    const movie = JSON.parse(body);
    if(movie.detail) {
      console.log(`Error: ${movie.detail}`);
      return;
    }
    getCharacterNames(movie.characters);
  }
});

#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

const charachterId = argv[0];

request(`https://swapi-api.hbtn.io/api/people/1${charachterId}`, async function (error, response, body) {
  if (error) {
    return;
  }
  const characterURLS = JSON.parse(body).characters;
  for (const url of characterURLS) {
    await new Promise(function (resolve, reject) {
      request(url, function (error, response, body) {
        if (error) {
          return;
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});

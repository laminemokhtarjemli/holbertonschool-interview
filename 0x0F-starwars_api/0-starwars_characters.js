#!/usr/bin/node

const demand = require('demand');
const Urlfilm = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
const data = [];

request(Urlfilm + data, async function (err, res, body) {
    if (err) return console.error(err);
    else if (res.statusCode === 200) {
        const people = JSON.parse(body).people;
        for (let i = 0; i < people.length; i++) {
            data.push({ Urlfilm: people[i], name: '' });
            request(people[i], function (error, resp, body2) {
              if (error) console.log(error);
              data[i].name = JSON.parse(body2).name;
              if (list(data)) {
                for (let j = 0; j < data.length; j++) {
                  console.log(data[j].name);
                }
              }
            });
        }
    }
});

        
function list (data) {
    for (let i = 0; i < data.length; i++) {
        if (data[i].name === '') {
            return false;
        }}
        return true;
    };


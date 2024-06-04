#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Failed to fetch movie data:', error);
    return;
  }

  const charactersList = JSON.parse(body).characters;
  const characterNames = [];

  const fetchCharacter = (index) => {
    if (index >= charactersList.length) {
      characterNames.forEach(name => console.log(name));
      return;
    }

    const characterUrl = charactersList[index];
    request(characterUrl, (error2, response2, body2) => {
      if (error2) {
        console.error('Failed to fetch character data:', error2);
        return;
      }

      const characterInfo = JSON.parse(body2).name;
      characterNames.push(characterInfo);
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});

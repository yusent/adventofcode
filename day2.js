const fs = require('fs');

fs.readFile('day2-input', 'utf8', (error, data) => {
  const validPasswordsCount = data
    .split('\n')
    .reduce((count, line) => {
      return line && checkPasswordLine(line) ? count + 1 : count;
    }, 0);

  console.log(validPasswordsCount);
});

const checkPasswordLine = line => {
  const [_, min, max, char, password] = /^(\d+)-(\d+) (\w): (\w+)$/.exec(line);
  const occurrences = (password.match(new RegExp(char, 'g')) || []).length;

  return occurrences >= min && occurrences <= max;
};

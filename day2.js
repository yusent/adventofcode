const fs = require('fs');

fs.readFile('day2-input', 'utf8', (error, data) => {
  const lines = data.split('\n');
  const validPasswordsCount1 = lines
    .reduce((count, line) => {
      return line && checkPasswordLine1(line) ? count + 1 : count;
    }, 0);
  const validPasswordsCount2 = lines
    .reduce((count, line) => {
      return line && checkPasswordLine2(line) ? count + 1 : count;
    }, 0);

  console.log('Part 1:', validPasswordsCount1);
  console.log('Part 2:', validPasswordsCount2);
});

const checkPasswordLine1 = line => {
  const [_, min, max, char, password] = /^(\d+)-(\d+) (\w): (\w+)$/.exec(line);
  const occurrences = (password.match(new RegExp(char, 'g')) || []).length;

  return occurrences >= min && occurrences <= max;
};

const checkPasswordLine2 = line => {
  const [_, pos0, pos1, char, password] = /^(\d+)-(\d+) (\w): (\w+)$/.exec(line);

  if (password[pos0 - 1] === char)
    return password[pos1 - 1] !== char;
  else
    return password[pos1 - 1] === char;
};

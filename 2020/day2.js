const fs = require('fs');

fs.readFile('day2-input', 'utf8', (_, data) => {
  const cases = data.trim().split('\n').map(parseLine);

  console.log('Part 1:', count(cases, check1));
  console.log('Part 2:', count(cases, check2));
});

const parseLine = line => {
  const [_, l, r, char, password] = /^(\d+)-(\d+) (\w): (\w+)$/.exec(line);
  return { l, r, char, password };
};

const check1 = ({ l, r, char, password }) => {
  const match = password.match(new RegExp(char, 'g'));
  return match && between(match.length, l, r);
};

const check2 = ({ l, r, char, password }) => (
  xor(password[l - 1] === char, password[r - 1] === char)
);

const count = (list, pred) => list.reduce((c, x) => pred(x) ? c + 1 : c, 0);
const between = (x, l, r) => x >= l && x <= r;
const xor = (cond0, cond1) => cond0 ? !cond1 : cond1;

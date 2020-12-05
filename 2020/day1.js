const fs = require('fs');

fs.readFile('input/day1', 'utf8', (_, data) => {
  const expenses = data.split('\n').map(Number);
  console.log('Part 1:', findPairMultiplication(expenses));
  console.log('Part 2:', findTripleMultiplication(expenses));
});

const findPairMultiplication = values => {
  const prev = new Set();

  for (const value of values) {
    const complement = 2020 - value;

    if (prev.has(complement))
      return value * complement;
    else
      prev.add(value);
  }
};

const findTripleMultiplication = values => {
  const sums = { [values[0] + values[1]]: values.slice(0,2) };
  const len = values.length;

  for (let i in values) {
    const complement = 2020 - values[i];

    if (sums[complement])
      return sums[complement][0] * sums[complement][1] * values[i];

    for (let j = 0; j < i; j++)
      sums[values[i] + values[j]] = [values[i], values[j]];
  }
};

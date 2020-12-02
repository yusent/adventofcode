const fs = require('fs');

fs.readFile('day1-input', 'utf8', (_, data) => {
  const expenses = new Set(data.split('\n').map(Number));
  console.log('Part 1', findPairMultiplication(2020, expenses));
  console.log('Part 2', findTripleMultiplication(expenses));
});

const findPairMultiplication = (sum, values) => {
  for (const value of values) {
    const complement = sum - value;

    if (values.has(complement))
      return value * complement;
  }
};

const findTripleMultiplication = values => {
  for (const value of values) {
    const complement = 2020 - value;
    const pairMult = findPairMultiplication(complement, values);

    if (pairMult)
      return value * pairMult;
  }
};

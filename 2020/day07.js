const fs = require('fs');

fs.readFile('input/day07', 'utf8', (_, data) => {
  const colors = data.trim().split('\n').reduce((acc, line) => ({
    ...acc,
    ...parseLine(line)
  }));

  const countBagsIn = (color, factor = 1) => Object
    .entries(colors[color])
    .reduce((count, [subColor, qty]) => (
      count + factor * qty + countBagsIn(subColor, factor * qty)
    ), 0);

  console.log('Part 1:', filterBags(colors).length);
  console.log('Part 2:', countBagsIn('shiny gold'));
});

const parseLine = line => {
  const [_, color, contents] = line.match(/^(\S+ \S+) bags contain (.*)\.$/);

  return {
    [color]: contents.split(', ').reduce((acc, content) => {
      const match = content.match(/^(\d+) (\S+ \S+) bags?$/);
      return match ? { ...acc, [match[2]]: match[1] } : acc;
    }, {}),
  };
};

const filterBags = (colors, bagsAcc = []) => {
  const [newBagsAcc, keepGoing] = Object
    .entries(colors)
    .reduce(colorsReducer, [bagsAcc, false]);

  return keepGoing ? filterBags(colors, newBagsAcc) : newBagsAcc;
};

const colorsReducer = ([bagsAcc, keepGoing], [color, subColors]) => Object
  .keys(subColors)
  .reduce(subColorsReducer(color, bagsAcc), [bagsAcc, keepGoing]);

const subColorsReducer = (color, bagsAcc) => ([acc, keep], k) => (
  (k === 'shiny gold' || bagsAcc.includes(k)) && !acc.includes(color)
    ? [[...acc, color], true]
    : [acc, keep]
);

const fs = require('fs');

fs.readFile('input/day10', 'utf8', (_, data) => {
  const numbers = data.trim().split('\n').map(Number).sort((a, b) => a - b);
  const adapters = [0, ...numbers, numbers[numbers.length - 1] + 3];

  let oneDiffs = 0;
  let threeDiffs = 0;

  for (let i = 1; i < adapters.length; i++)
    if (adapters[i] - 1 === adapters[i - 1])
      oneDiffs ++;
    else if (adapters[i] - 3 === adapters[i - 1])
      threeDiffs ++;

  console.log('Part 1:', oneDiffs * threeDiffs);

  const countArrangementsFrom = (i, possibleArrangements = {}) => {
    if (i == adapters.length - 1) return 1;
    if (possibleArrangements[i]) return possibleArrangements[i];

    let ans = 0;

    for (let j = i + 1; j < adapters.length && adapters[j] - adapters[i] <= 3; j++)
      ans += countArrangementsFrom(j, possibleArrangements);

    possibleArrangements[i] = ans
    return ans;
  };

  console.log('Part 2:', countArrangementsFrom(0));
});

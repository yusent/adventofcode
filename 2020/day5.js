const fs = require('fs');

fs.readFile('day5-input', 'utf8', (_, data) => {
  const seats = data.trim().split('\n').map(seatID).sort((a, b) => b - a);

  console.log('Part 1:', seats[0]);

  for (let i = seats.length - 1; i >= 0; i--) {
    if (seats[i - 1] !== seats[i] + 1) {
      console.log('Part 2:', seats[i] + 1);
      break;
    }
  }
});

const seatID = str => getRow(str) * 8 + getCol(str);
const getRow = str => binarySpacePos('B', str.slice(0, 7));
const getCol = str => binarySpacePos('R', str.slice(7));

const binarySpacePos = (upperChar, str) => {
  const chars = str.split('');
  const len = chars.length;

  return chars.reduce((pos, char, index) => (
    char == upperChar ? pos + 2 ** (len - index - 1) : pos
  ), 0);
};

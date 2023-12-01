const fs = require('fs');
const input = fs.readFileSync('input/day01', 'utf8');
const lines = input.trim().split('\n');
const calibrationValue = line => Number(line[0] + line.slice(-1));

const wordsToDigits = (line) => {
  if (line == '') return '';
  if (line.startsWith('one')) return '1' + wordsToDigits(line.slice(2));
  if (line.startsWith('two')) return '2' + wordsToDigits(line.slice(2));
  if (line.startsWith('three')) return '3' + wordsToDigits(line.slice(4));
  if (line.startsWith('four')) return '4' + wordsToDigits(line.slice(4));
  if (line.startsWith('five')) return '5' + wordsToDigits(line.slice(3));
  if (line.startsWith('six')) return '6' + wordsToDigits(line.slice(3));
  if (line.startsWith('seven')) return '7' + wordsToDigits(line.slice(4));
  if (line.startsWith('eight')) return '8' + wordsToDigits(line.slice(4));
  if (line.startsWith('nine')) return '9' + wordsToDigits(line.slice(3));
  if (/^\d/.test(line)) return line[0] + wordsToDigits(line.slice(1));
  return wordsToDigits(line.slice(1));
};

console.log(`Part 1: ${lines.reduce((acc, line) => acc + calibrationValue(line.replace(/\D/g, '')), 0)}`);
console.log(`Part 2: ${lines.reduce((acc, line) => acc + calibrationValue(wordsToDigits(line)), 0)}`);

const fs = require('fs');

fs.readFile('day3-input', 'utf8', (_, data) => {
  const rows = data.trim().split('\n');
  const height = rows.length;
  const width = rows[0].length;

  const count = (right, down, x = right, y = down, trees = 0) => {
    if (y >= height) return trees;

    const inc = rows[y][x] == "#" ? 1 : 0;

    return count(right, down, (x + right) % width, y + down, trees + inc);
  }

  const part1 = count(3, 1);
  const part2 = part1 * count(1, 1) * count(5, 1) * count(7, 1) * count(1, 2);

  console.log('Part 1:', part1);
  console.log('Part 2:', part2);
});

const fs = require('fs');

fs.readFile('day3-input', 'utf8', (_, data) => {
  const rows = data.trim().split('\n');
  const height = rows.length;
  const width = rows[0].length;

  const countTrees = (right, down, x = right, y = down, trees = 0) => {
    if (y >= height) return trees;

    return countTrees(
      right,
      down,
      (x + right) % width,
      y + down,
      trees + (rows[y][x] == "#" ? 1 : 0)
    );
  }

  const part1 = countTrees(3, 1);
  const part2 = [[1, 1], [5, 1], [7, 1], [1, 2]].reduce(
    (acc, [right, down]) => acc * countTrees(right, down),
    part1
  );

  console.log('Part 1:', part1);
  console.log('Part 2:', part2);
});

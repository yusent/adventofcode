const fs = require('fs');

fs.readFile('input/day11', 'utf8', (_, data) => {
  const layout = data.trim().split('\n').map(l => l.split(''));

  console.log('Part 1:', count(layout));
  console.log('Part 2:', count(layout, true));
});

const count = (prev, rule2 = false, prevJSON = JSON.stringify(prev)) => {
  const state = nextRound(prev, rule2);
  const json = JSON.stringify(state);

  return json == prevJSON
    ? state.reduce((acc, row) => acc + row.filter(c => c == '#').length, 0)
    : count(state, rule2, json);
};

const nextRound = (layout, rule2) => layout.map((row, y) => {
  return row.map((cell, x) => {
    if (cell == '.') return '.';

    let neighboursCount = 0;

    for (let offX = -1; offX < 2; offX++) {
      for (let offY = -1; offY < 2; offY++) {
        if (offX == 0 && offY == 0) continue;

        neighboursCount += findSeat(layout, x, y, offX, offY, rule2);
      }
    }

    if (cell == 'L' && neighboursCount == 0) return '#';

    if (cell == '#' && neighboursCount >= 4 + rule2) return 'L';

    return cell;
  });
});

const findSeat = (layout, x, y, offsetX, offsetY, rule2) => {
  switch (layout[y + offsetY] && layout[y + offsetY][x + offsetX]) {
    case '.':
      return rule2
        ? findSeat(layout, x + offsetX, y + offsetY, offsetX, offsetY, rule2)
        : 0;

    case '#':
      return 1;
  }

  return 0;
};

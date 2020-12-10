const fs = require('fs');

fs.readFile('input/day8', 'utf8', (_, data) => {
  const instructions = data.trim().split('\n');
  const [__, output] = evaluate(instructions);
  const fixedOutput = fix(instructions);

  console.log('Part 1:', output);
  console.log('Part 2:', fixedOutput);
});

const evaluate = instructions => {
  let acc = 0;
  let prev = [];

  for (let i = 0; i < instructions.length; i++) {
    if (prev.includes(i)) return [false, acc];

    prev.push(i);

    const [cmd, x] = instructions[i].split(' ');
    const offset = Number(x);

    if (cmd === 'acc')
      acc += offset;
    else if (cmd === 'jmp')
      i += offset - 1;
  }

  return [true, acc];
};

const fix = instructions => {
  for (let i = 0; i < instructions.length; i++) {
    if (/acc/.test(instructions[i])) continue;

    let modifiedInstructions = [...instructions];
    modifiedInstructions[i] = /jmp/.test(modifiedInstructions[i])
      ? modifiedInstructions[i].replace('jmp', 'nop')
      : modifiedInstructions[i].replace('nop', 'jmp');

    const [terminated, result] = evaluate(modifiedInstructions);

    if (terminated) return result;
  }
};

const changeCMD = cmd => cmd === 'jmp' ? 'nop' : 'jmp';

const fs = require('fs');

fs.readFile('day4-input', 'utf8', (_, data) => {
  const [part1, part2] = data.trim().split('\n\n').reduce(([c1, c2], str) => {
    const passport = parsePassport(str);
    const passedCheck1 = check1(passport);

    return [c1 + passedCheck1, c2 + (passedCheck1 && check2(passport))];
  }, [0, 0]);

  console.log('Part 1:', part1);
  console.log('Part 2:', part2);
});

const required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];

const parsePassport = string => Object.fromEntries(
  string.split(/\s+/).map(x => x.split(':'))
);

const check1 = passport => required.every(x => x in passport);

const check2 = passport => Object.entries(passport).every(([key, val]) => {
  const intVal = parseInt(val);

  switch (key) {
    case 'byr':
      return intVal >= 1920 && intVal <= 2002;

    case 'iyr':
      return intVal >= 2010 && intVal <= 2020;

    case 'eyr':
      return intVal >= 2020 && intVal <= 2030;

    case 'hgt':
      const formatMatch = val.match(/(cm|in)$/);

      if (formatMatch) {
        if (formatMatch[0] === 'cm')
          return intVal >= 150 && intVal <= 193;
        else
          return intVal >= 59 && intVal <= 76;
      }

      return false;

    case 'hcl':
      return /^#[0-9a-f]{6}$/.test(val);

    case 'ecl':
      return /^(amb|blu|brn|gry|grn|hzl|oth)$/.test(val);

    case 'pid':
      return /^\d{9}$/.test(val);

    default:
      return true;
  }
});

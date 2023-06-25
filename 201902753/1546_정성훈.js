const [N, input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const arr = input.split(" ").map(v => +v).sort((a, b) => a - b);

const MAX = arr[+N - 1];

const avg = arr.reduce((acc, cur) => {
  return acc += (cur / MAX) * 100;
}, 0) / +N

console.log(avg);

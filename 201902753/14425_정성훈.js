const [num, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = num.split(" ").map(Number);
const map = new Map();
let count = 0;

for (let i = 0; i < N; i++) {
  map.set(input[i], true);
}

for (let i = N; i < N + M; i++) {
  if (map.has(input[i])) {
    count++;
  }
}

console.log(count);

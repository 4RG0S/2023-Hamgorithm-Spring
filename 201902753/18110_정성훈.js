const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const exclusion = Math.round(+N * 0.15);
const arr = input.map(v => parseInt(v)).sort((a, b) => a - b);
let sum = 0;

for(let i = exclusion; i<(N - exclusion); i++) {
  sum += arr[i];
}
console.log(sum === 0 ? 0 : Math.round(sum / (N - (exclusion * 2))));
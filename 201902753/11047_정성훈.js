const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [coins, won] = N.split(" ").map((v) => parseInt(v));
let count = 0;
for (let i = coins - 1; i >= 0; i--) {
  if (won <= 0) break;
  if (+input[i] > won) continue;
  count += parseInt(won / +input[i]);
  won %= +input[i];
}

console.log(count);

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map((v) => parseInt(v));
const arr = input[1].split(" ").map((v) => parseInt(v));
const prefixSum = Array(N + 1).fill(0);
const result = [];

for (let i = 1; i <= N; i++) {
  prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
}

for (let i = 2; i < 2 + M; i++) {
  const [start, end] = input[i].split(" ").map((v) => parseInt(v));
  result.push(prefixSum[end] - prefixSum[start - 1]);
}

console.log(result.join("\n"));

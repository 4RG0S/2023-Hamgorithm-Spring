const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map((v) => +v);
const [N2, M2] = input[N + 1].split(" ").map((v) => +v);

const A = [];
const B = [];

for (let i = 1; i <= N; i++) {
  A.push(input[i].split(" "));
}

for (let i = 2 + N; i < 2 + N + N2; i++) {
  B.push(input[i].split(" "));
}

const result = Array.from(Array(N), () => Array(M2).fill(0));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M2; j++) {
    for (let k = 0; k < M; k++) {
      result[i][j] += A[i][k] * B[k][j];
    }
  }
}

console.log(result.map((row) => row.join(" ")).join("\n"));

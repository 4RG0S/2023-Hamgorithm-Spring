const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const answer = [...input[0]].sort((a, b) => b - a);

console.log(answer.join(""));

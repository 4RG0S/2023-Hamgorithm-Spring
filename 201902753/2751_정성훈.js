const fs = require("fs");
const [N, ...input] = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n")
  .map((v) => Number(v));
const sortArr = input.sort((a, b) => a - b);
console.log(sortArr.join("\n"));

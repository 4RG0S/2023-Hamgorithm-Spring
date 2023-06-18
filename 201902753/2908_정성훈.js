const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ");

const arr = input
  .map((v) => v.split("").reverse().join(""))
  .map((v) => parseInt(v))
  .sort((a, b) => a - b);

console.log(arr[1]);

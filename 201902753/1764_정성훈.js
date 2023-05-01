const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [listenN, seeN] = N.split(" ").map((v) => parseInt(v));

const listenSet = new Set(input.slice(0, listenN));
const seeSet = new Set(input.slice(listenN));
const result = [...listenSet].filter((v) => seeSet.has(v)).sort();
console.log(
  result.length === 0 ? "0" : `${result.length}\n${result.join("\n")}`
);

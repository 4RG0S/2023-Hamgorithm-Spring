const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [save, find] = N.split(" ").map((v) => parseInt(v));
const info = {};

for (let i = 0; i < save; i++) {
  const [site, pw] = input[i].split(" ");
  info[site] = pw;
}

const result = [];
for (let i = save; i < save + find; i++) {
  result.push(info[input[i]]);
}

console.log(result.join("\n"));

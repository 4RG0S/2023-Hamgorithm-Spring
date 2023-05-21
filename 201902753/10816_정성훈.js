const [N, have, M, find] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const haveArr = have.split(" ");

const findArr = find.split(" ");

const countMap = {};
haveArr.forEach((value) => {
  countMap[value] = (countMap[value] || 0) + 1;
});
let log = [];
findArr.forEach((v) => {
  const count = countMap[v] || 0;
  log.push(count);
});

console.log(log.join("\n"));

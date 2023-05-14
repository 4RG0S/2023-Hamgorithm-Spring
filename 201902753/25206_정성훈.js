const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const gradePointAvg = {
  "A+": 4.5,
  A0: 4.0,
  "B+": 3.5,
  B0: 3.0,
  "C+": 2.5,
  C0: 2.0,
  "D+": 1.5,
  D0: 1.0,
  F: 0.0,
};
let total = 0;
const N = input.length;
const sum = input.reduce((acc, cur) => {
  let [, avg, grade] = cur.split(" ");
  avg = Number(avg);
  if (grade === "P") {
    return acc;
  }
  total += avg;
  return (acc += avg * gradePointAvg[grade]);
}, 0);

console.log(sum / total);

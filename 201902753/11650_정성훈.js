const fs = require("fs");
const [N, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const coordsArr = input.map((coords) =>
  coords.split(" ").map((v) => Number(v))
);

coordsArr.sort((a, b) => {
  if (a[0] === b[0]) {
    return a[1] - b[1];
  } else {
    return a[0] - b[0];
  }
});

console.log(coordsArr.map((v) => v.join(" ")).join("\n"));

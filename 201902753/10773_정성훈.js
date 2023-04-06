const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const result = [];
for (const o of input) {
  if (parseInt(o) === 0) {
    result.pop();
  } else {
    result.push(parseInt(o));
  }
}

console.log(
  result.reduce((acc, cur) => {
    return (acc += cur);
  }, 0)
);

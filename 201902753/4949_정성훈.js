const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const pair = {
  ")": "(",
  "]": "[",
  "}": "{",
};
let flag = false;
const result = [];
for (const line of input) {
  if (line === ".") break;
  flag = false;
  const stack = [];
  for (let i = 0; i < line.length; i++) {
    if (line[i] === "(" || line[i] === "[" || line[i] === "{") {
      stack.push(line[i]);
    } else if (line[i] === ")" || line[i] === "]" || line[i] === "}") {
      if (pair[line[i]] !== stack[stack.length - 1]) {
        result.push("no");
        flag = true;
        break;
      } else {
        stack.pop();
      }
    }
  }

  if (!flag) {
    stack.length !== 0 ? result.push("no") : result.push("yes");
  }
}
console.log(result.join("\n"));

const fs = require("fs");
const [N, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const stack = [];
const result = [];
input.forEach((v) => {
  const [command, num] = v.split(" ");
  switch (command) {
    case "push": {
      stack.push(parseInt(num));
      break;
    }

    case "pop": {
      result.push(stack.length === 0 ? -1 : stack.pop());
      break;
    }

    case "size": {
      result.push(stack.length);
      break;
    }

    case "empty": {
      result.push(stack.length === 0 ? 1 : 0);
      break;
    }

    case "top": {
      result.push(stack.length === 0 ? -1 : stack[stack.length - 1]);
      break;
    }
  }
});

console.log(result.join("\n"));

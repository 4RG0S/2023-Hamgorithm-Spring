const [T, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const answer = [];

for (let i = 0; i < input.length; i += 3) {
  const commands = input[i];
  const N = +input[1 + i];
  const arr = JSON.parse(input[i + 2]);

  let revFlag = false;
  let flag = false;
  let start = 0;
  let end = N - 1;

  for (const command of commands) {
    switch (command) {
      case "R":
        revFlag = !revFlag;
        break;
      case "D":
        if (start > end) {
          flag = true;
          break;
        }
        if (revFlag) {
          end--;
        } else {
          start++;
        }
    }
  }

  const output = arr.slice(start, end + 1);
  answer.push(
    flag ? "error" : JSON.stringify(revFlag ? output.reverse() : output)
  );
}

console.log(answer.join("\n"));

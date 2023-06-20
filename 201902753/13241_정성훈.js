const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];

rl.on("line", function (line) {
  lines.push(line);
}).on("close", function () {
  const [A, B] = lines[0].split(" ").map((v) => BigInt(v));
  const gcd = (a, b) => {
    while (b !== 0n) {
      let temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  };

  let divisor = gcd(A, B);
  console.log((A / divisor) * B);
});

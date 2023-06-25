const gcd = (a, b) => {
  if (b === 0) return a;
  return gcd(b, a % b);
};

const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const result = [];

for (const v of input) {
  const [a, b] = v.split(" ").map((i) => parseInt(i));
  const lcm = (a * b) / gcd(a, b);
  result.push(lcm);
}

console.log(result.join("\n"));

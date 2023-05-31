function gcd(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

const [A, B] = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const [A_numerator, A_denominator] = A.split(" ").map(v => parseInt(v));
const [B_numerator, B_denominator] = B.split(" ").map(v => parseInt(v));

let AB_numerator = (A_numerator * B_denominator) + (B_numerator * A_denominator);
let AB_denominator = A_denominator * B_denominator;

const div = gcd(AB_numerator, AB_denominator);

AB_numerator /= div;
AB_denominator /= div;

console.log(`${AB_numerator} ${AB_denominator}`);

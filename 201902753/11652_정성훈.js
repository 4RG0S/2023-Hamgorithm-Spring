const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const cards = new Map();

for (let i = 1; i <= N; i++) {
  const card = BigInt(input[i]);
  if (cards.has(card)) {
    cards.set(card, cards.get(card) + 1n);
  } else {
    cards.set(card, 1n);
  }
}

let maxCount = 0n;
let maxCard = 0n;

for (let [card, count] of cards) {
  if (count > maxCount || (count === maxCount && card < maxCard)) {
    maxCount = count;
    maxCard = card;
  }
}

console.log(maxCard.toString());

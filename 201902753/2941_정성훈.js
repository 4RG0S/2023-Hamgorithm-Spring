let input = require("fs").readFileSync("/dev/stdin").toString().trim();

const croatianAlphabet = {
  "c=": "1",
  "c-": "2",
  "dz=": "3",
  "d-": "4",
  lj: "5",
  nj: "6",
  "s=": "7",
  "z=": "8",
};

for (const k in croatianAlphabet) {
  if (input.includes(k)) {
    input = input.replaceAll(k, croatianAlphabet[k]);
  }
}

console.log(input.length);

let input = Number(require("fs").readFileSync("/dev/stdin").toString().trim());

let n = 1;
while (input > n) {
  input -= n;
  n++;
}

if (n % 2 === 0) {
  console.log(`${input}/${n - input + 1}`);
} else {
  console.log(`${n - input + 1}/${input}`);
}

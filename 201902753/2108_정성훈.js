const [n, ...input] = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const N = parseInt(n);

const map = {};
let max = 0;
for(const key of input) {
 map[key]  = (map[key] || 0) + 1
 if (max < map[key]) {
  max = map[key];
 }
}
let maxKeys = [];
for(const key in map) {
  if(map[key] === max) {
    maxKeys.push(Number(key));
  }
}
maxKeys.sort((a, b) => a - b);
const arr = input.map(v => parseInt(v)).sort((a, b) => a - b);

const mean = Math.round((arr.reduce((acc, cur) => {return acc += cur}, 0)) / N);
const mid = arr[Math.floor(N/2)];
const most = (maxKeys.length > 1) ? maxKeys[1] : maxKeys[0];
const range = Math.abs(arr[N-1] - arr[0])

console.log([mean, mid, most, range].join("\n"));
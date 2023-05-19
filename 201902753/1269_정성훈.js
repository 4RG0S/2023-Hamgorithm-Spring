const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const A = new Set(...[input[1].split(" ")]);
const B = new Set(...[input[2].split(" ")]);

const Amap = [];
const Bmap = [];

A.forEach(v => {
  if(!B.has(v)) {
    Amap.push(v);
  }
})

B.forEach(v => {
  if(!A.has(v)) {
    Bmap.push(v);
  }
})
console.log(Amap.length + Bmap.length);
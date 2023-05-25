const [state, ...list] = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, M] = state.split(" ").map(v => parseInt(v));

const name = {};
const num = [];

for(let i = 0; i<N; i++) {
  name[list[i]] = i + 1;
  num[i] = list[i];
}
const result = [];

for(let i = N; i<N+M; i++) {
  if(isNaN(Number(list[i]))) {
    result.push(name[list[i]]);
  } else {
    result.push(num[Number(list[i]) - 1]);
  }
}

console.log(result.join("\n"));
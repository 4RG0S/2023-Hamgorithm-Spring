const [N,...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const arr = input.map(v => v.split(' '));
const dance = new Set(["ChongChong"]);

for(let i = 0; i<+N; i++) {
  if(dance.has(arr[i][0]) || dance.has(arr[i][1])) {
    dance.add(arr[i][0]);
    dance.add(arr[i][1]);
  }
}

console.log(dance.size);
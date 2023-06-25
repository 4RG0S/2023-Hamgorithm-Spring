const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const dp = [];

for(let i = 0; i<+N; i++) {
 dp.push(input[i].split(" ").map(v => parseInt(v)));
}

for(let i = 1; i<+N; i++) {
  dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + dp[i][0];
  dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + dp[i][1];
  dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + dp[i][2];
}
console.log(Math.min(dp[+N-1][0], Math.min(dp[+N-1][1], dp[+N-1][2])));
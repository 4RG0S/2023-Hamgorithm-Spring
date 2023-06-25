const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const company = {};
const answer = [];

input.forEach((v) => {
  const [name, log] = v.split(" ");
  if(log === "enter") {
    company[name] = true;
  } else {
    company[name] = false;
  }
})

for(const name in company) {
  if(company[name]) {
    answer.push(name);
  }
}

answer.sort().reverse();

console.log(answer.join("\n"));
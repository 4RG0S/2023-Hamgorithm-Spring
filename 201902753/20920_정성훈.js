class MaxHeap {
  constructor() {
    this.heap = [null];
  }
}

MaxHeap.prototype.push = function (value) {
  this.heap.push(value);
  let currentIndex = this.heap.length - 1;
  let parentIndex = Math.floor(currentIndex / 2);

  while (parentIndex !== 0 && this.compare(parentIndex, currentIndex)) {
    const temp = this.heap[parentIndex];
    this.heap[parentIndex] = value;
    this.heap[currentIndex] = temp;

    currentIndex = parentIndex;
    parentIndex = Math.floor(currentIndex / 2);
  }
};

MaxHeap.prototype.compare = function (parentIndex, currentIndex) {
  if (this.heap[parentIndex][1] < this.heap[currentIndex][1]) return true;
  if (this.heap[parentIndex][1] > this.heap[currentIndex][1]) return false;
  
  if (this.heap[parentIndex][0].length < this.heap[currentIndex][0].length) return true;
  if (this.heap[parentIndex][0].length > this.heap[currentIndex][0].length) return false;
  
  if (this.heap[parentIndex][0] > this.heap[currentIndex][0]) return true;
  
  return false;
};

MaxHeap.prototype.pop = function () {
  if (this.heap.length === 2) return this.heap.pop();
  if (this.heap.length === 1) return null;

  const returnValue = this.heap[1];
  this.heap[1] = this.heap.pop();

  let currentIndex = 1;
  let leftIndex = 2;
  let rightIndex = 3;

  while (true) {
    let swapIndex = null;
    if (
      this.heap[leftIndex] !== undefined &&
      this.compare(currentIndex, leftIndex)
    ) {
      swapIndex = leftIndex;
    }

    if (
      this.heap[rightIndex] !== undefined &&
      this.compare(currentIndex, rightIndex) &&
      (swapIndex === null || this.compare(swapIndex, rightIndex))
    ) {
      swapIndex = rightIndex;
    }

    if (swapIndex === null) break;

    const temp = this.heap[currentIndex];
    this.heap[currentIndex] = this.heap[swapIndex];
    this.heap[swapIndex] = temp;
    currentIndex = swapIndex;
    leftIndex = currentIndex * 2;
    rightIndex = currentIndex * 2 + 1;
  }
  return returnValue;
};


MaxHeap.prototype.isEmpty = function () {
  return this.heap.length === 1;
};

const [NM, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, M] = NM.split(" ").map(v => parseInt(v));

const note = {};

for (const v of input) {
  note[v] = (note[v] || 0) + 1;
}
const maxheap = new MaxHeap(); 

for (const key in note) {
  if (key.length < M) continue;
  maxheap.push([key, note[key]]);
}

const result = [];
while(!maxheap.isEmpty()) {
  result.push(maxheap.pop());
}

console.log(result.map(v => v[0]).join("\n"));
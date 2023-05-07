class Node {
  constructor(value) {
    this.next = null;
    this.value = value;
  }
}
class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(newValue) {
    const node = new Node(newValue);
    if (this.size === 0) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }

  pop() {
    if (this.size === 0) {
      return -1;
    }
    const ret = this.head.value;
    this.head = this.head.next;
    this.size--;
    return ret;
  }

  getFrontValue() {
    if (this.size === 0) return -1;
    return this.head.value;
  }

  getBackValue() {
    if (this.size === 0) return -1;
    return this.tail.value;
  }

  getSize() {
    return this.size;
  }

  isEmpty() {
    return this.size === 0 ? 1 : 0;
  }
}

const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const queue = new Queue();
const result = [];
for (const line of input) {
  const [command, value] = line.split(" ");
  switch (command) {
    case "push":
      queue.push(value);
      break;
    case "pop":
      result.push(queue.pop());
      break;
    case "front":
      result.push(queue.getFrontValue());
      break;
    case "back":
      result.push(queue.getBackValue());
      break;
    case "size":
      result.push(queue.getSize());
      break;
    case "empty":
      result.push(queue.isEmpty());
      break;
  }
}

console.log(result.join("\n"));

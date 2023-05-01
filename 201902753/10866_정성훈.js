class Node {
  constructor(value) {
    this.next = null;
    this.prev = null;
    this.value = value;
  }
}

class Deque {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push_front(newValue) {
    const node = new Node(newValue);
    if (this.size === 0) {
      this.head = node;
      this.tail = node;
    } else {
      this.head.prev = node;
      node.next = this.head;
      this.head = node;
    }
    this.size++;
  }

  push_back(newValue) {
    const node = new Node(newValue);
    if (this.size === 0) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.size++;
  }

  pop_front() {
    if (this.size === 0) return -1;
    const value = this.head.value;
    this.head = this.head.next;
    this.size--;
    return value;
  }

  pop_back() {
    if (this.size === 0) return -1;
    const value = this.tail.value;
    this.tail = this.tail.prev;
    this.size--;
    return value;
  }

  front() {
    if (this.size === 0) return -1;
    return this.head.value;
  }

  back() {
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

const deque = new Deque();
const result = [];
for (const line of input) {
  const [command, value] = line.split(" ");
  switch (command) {
    case "push_front":
      deque.push_front(value);
      break;
    case "push_back":
      deque.push_back(value);
      break;
    case "pop_front":
      result.push(deque.pop_front());
      break;
    case "pop_back":
      result.push(deque.pop_back());
      break;
    case "front":
      result.push(deque.front());
      break;
    case "back":
      result.push(deque.back());
      break;
    case "size":
      result.push(deque.getSize());
      break;
    case "empty":
      result.push(deque.isEmpty());
      break;
  }
}

console.log(result.join("\n"));

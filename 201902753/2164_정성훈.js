const input = Number(
  require("fs").readFileSync("/dev/stdin").toString().trim()
);

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  append(newValue) {
    const newNode = new Node(newValue);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size += 1;
  }

  getHead() {
    return this.head.value;
  }

  removeHead() {
    this.head = this.head.next;
    this.size--;
  }
  getSize() {
    return this.size;
  }
}

const list = new SinglyLinkedList();
for (let i = 1; i <= input; i++) {
  list.append(i);
}
while (list.getSize() !== 1) {
  list.removeHead();
  list.append(list.getHead());
  list.removeHead();
}

console.log(list.getHead());

import sys
from typing import Optional, Any


class Node:
    def __init__(
        self,
        data: Any = None,
    ):
        super().__init__()
        self.data: Any = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def remove_next(self):
        assert self.next is not None and self.next.next is not None
        self.next = self.next.next
        self.next.prev = self

    def remove_prev(self):
        assert self.prev is not None and self.prev.prev is not None
        self.prev = self.prev.prev
        self.prev.next = self

    def return_next_nodes(self):
        result = [self.data]
        p = self.next
        while p is not None and p.data is not None:
            result.append(p.data)
            p = p.next
        return result

    def return_prev_nodes(self):
        result = [self.data]
        p = self.prev
        while p is not None and p.data is not None:
            result.append(p.data)
            p = p.prev
        return result


def link_two_nodes(first: Node, second: Node):
    first.next = second
    second.prev = first


def solve(commands: list[str], arr: list[int]):
    head = Node()
    tail = Node()

    reversed_order = False
    length = 0

    link_two_nodes(head, tail)

    for elem in arr:
        length += 1
        node = Node(elem)
        assert tail.prev is not None
        node.prev = tail.prev
        node.prev.next = node
        node.next = tail
        node.next.prev = node

    for command in commands:
        if command == "R":
            reversed_order = not reversed_order
        elif command == "D":
            if length == 0:
                print("error")
                break
            length -= 1
            if reversed_order:
                tail.remove_prev()
            else:
                head.remove_next()
    else:
        assert head.next is not None
        assert tail.prev is not None
        if head.next == tail:
            print([])
        else:
            if reversed_order:
                print("[" + ",".join(map(str, tail.prev.return_prev_nodes())) + "]")
            else:
                print("[" + ",".join(map(str, head.next.return_next_nodes())) + "]")


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        commands = list(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline())
        str_formed_array = sys.stdin.readline().rstrip()[1:-1]
        if str_formed_array == "":
            integer_array = []
        else:
            integer_array = list(map(int, str_formed_array.split(",")))

        solve(commands, integer_array)

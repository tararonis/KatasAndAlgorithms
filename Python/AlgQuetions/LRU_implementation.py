import time


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    cashe_limit = 3

    def __init__(self, func):
        self.func = func
        self.cashe = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nect = self.tail
        self.tail.prev = self.head

    def __call__(self, *args, **kwargs):
        if args in self.cashe:
            self.llist(args)
            return f"Cached ...{self.cashe[args]}"

        if len(self.cashe) > self.cashe_limit:
            node = self.head.next
            self._remove(node)
            del self.cashe[node.key]

        result = self.func(*args, **kwargs)
        self.cashe[args] = result
        node = Node(args, result)
        self._add(node)
        return result

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    # If result in cache, move to top of Cache/linked list
    def llist(self, args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self._remove(node)
                self._add(node)
                break
            else:
                current = current.next


@LRUCache
def func(n):
    print(f"Computing...{n}x{n}")
    time.sleep(1)
    return n * n


def main():
    print(f"\nFunction: func")
    print(func(4))  # Cache: {(4,): 16}
    print(func(5))  # Cache: {(4,): 16, (5,): 25}
    print(func(4))  # Cache: {(5,): 25, (4,): 16}
    print(func(6))  # Cache: {(5,): 25, (4,): 16, (6,): 36}
    print(func(7))  # Cache: {(4,): 16, (6,): 36, (7,): 49}
    print(func(8))  # Cache: {(6,): 36, (7,): 49, (8,): 64}


if __name__ == "__main__":
    main()

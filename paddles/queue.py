# A linked list node is a list [item, next].
# These constants make the code more readable.
DATA = 0
NEXT = 1


class LinkedListQueue:
    """A queue implemented using a linked list.

    >>> q = LinkedListQueue("abc")
    >>> q.size()
    3
    >>> q.dequeue()
    'a'
    >>> q.front()
    'b'
    >>> q.enqueue("d")
    >>> print(q)
    LinkedListQueue(['b', 'c', 'd'])
    """

    def __init__(self, iterable=None):
        """Initialize this queue with the given items, if any."""
        self._head = None
        self._tail = None
        self._length = 0
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __str__(self):
        """Return a formatted string representation of this queue."""
        strings = []
        current = self._head
        while current:
            strings.append(f"'{current[DATA]}'")
            current = current[NEXT]
        return f"LinkedListQueue([{', '.join(strings)}])"

    def size(self):
        """Return the number of items in this queue."""
        return self._length

    def enqueue(self, item):
        """Insert the given item at the back of this queue."""
        node = [item, None]
        if self.size() == 0:
            self._head = node
            self._tail = node
        else:
            self._tail[NEXT] = node
            self._tail = node
        self._length += 1

    def front(self):
        """Return the item at the front of this queue without removing it."""
        if self.size() == 0:
            raise ValueError("can't access front of an empty queue")
        return self._head[DATA]

    def dequeue(self):
        """Remove and return the item at the front of this queue,

        or raise ValueError if this queue is empty.
        """
        if self.size() == 0:
            raise ValueError("can't dequeue from an empty queue")
        item = self._head[DATA]
        self._head = self._head[NEXT]
        self._length -= 1
        if self.size() == 0:
            self._tail = None
        return item

class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.nextnode = nextnode


class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):
        """ Initializes new Iterator """
        self.node = node
        self.emptynode = emptynode

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.node is None:
            raise StopIteration
        else:
            elem = self.node.elem
            self.node = self.node.nextnode
            return elem


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        """ head - start of queue (we remove element from here),
         tail - end of queue (we append new element here) """
        self.emptynode = QueueNode(None, None)
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, elem):
        """ Pushes 'elem' to queue """
        if self.size > 0:
            newtail = QueueNode(elem, None)
            self.tail.nextnode = newtail
            self.tail = newtail
        else:
            self.tail = QueueNode(elem, None)
            self.head = self.tail
        self.size += 1

    def pop(self):
        """ Removes front of queue and returns it """
        elem = self.head.elem
        newhead = self.head.nextnode
        self.head = newhead
        self.size -= 1
        return elem

    def front(self):
        """ Returns front of queue """
        return self.head.elem

    def empty(self):
        """ Checks whether queue is empty """
        return self.head is None

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.head, None)

    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.size

    def clear(self):
        """ Makes queue empty """
        self.head = None
        self.tail = None
        self.size = 0


if __name__ == '__main__':
    n = 5

    queue = LinkedQueue()
    for i in range(n):
        queue.push(i * 10)

    print(list(queue))

    queue.pop()

    print(list(queue))

    print(queue.__len__())

    print(queue.front())
    print(queue.empty())

    queue.clear()
    print(queue.empty())

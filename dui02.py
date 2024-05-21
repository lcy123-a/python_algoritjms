class Queue(object):
    def __init__(self):
        self._item = []

    def is_empty(self):
        return self._item == []
    
    def in_queue(self, item):
        self._item.append(item)

    def out_queue(self):
        return self._item.pop(0)
    
    def size(self):
        return self._item.__len__()
    
if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.in_queue(1)
    q.in_queue(2)
    q.in_queue(3)
    q.in_queue(4)
    print(q.is_empty())
    print(q.size())
    print(q.out_queue())
    print(q.out_queue())
    print(q.size())
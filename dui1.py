class HeapPriQueueError(ValueError):
    pass


class Heap_Pri_Queue(object):
    def __init__(self, elems = []):
        self._elems = list(elems)
        if self._elems:
            self.buildheap()

    # 判空
    def is_empty(self):
        return self._elems is []
    
    # 查看堆顶元素，即优先级最低元素
    def peek(self):
        if self.is_empty():
            raise HeapPriQueueError("in pop")
        return self._elems[0]
    
    # 将新的优先级加入队列 O(logn)
    def enqueue(self, e):
        # 在队列末尾创建一个空元素
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    # 新的优先级默认放在队尾，因此失去堆序，进行siftup构建堆序
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2    # j 为 i 的父节点
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    # 将堆顶值最小优先级最高的出队，确保弹出元素后仍然维持秩序
    # 将最后的元素放在堆顶，然后进行siftdown
    # O(logn)
    def dequeue(self):
        if self.is_empty():
            raise HeapPriQueueError("in pop")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j] > elems[j + 1]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    # 构建堆序 O(n)
    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)

if __name__ == "__main__":
    l = Heap_Pri_Queue([5, 6, 1, 2, 4, 8, 9, 0, 3, 7])
    print(l._elems) 
    l.dequeue()
    print(l._elems)
    print(l.is_empty())
    l.enqueue(0)
    print(l._elems)
    print(l.peek())
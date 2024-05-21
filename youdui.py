class ListPriQueueValueError(ValueError):
    pass

class List_Pri_Queue(object):
    def __init__(self, elems = []):
        self._elems = list(elems)
        # 从大到小排序，末尾值最小，但优先级最高，方便弹出且效率为O(1)
        self._elems.sort(reverse = True)

    # 判断队列是否为空
    def is_empty(self):
        return self._elems is []
    
    # 查看最高优先级O(1)
    def peek(self):
        if self.is_empty():
            raise ListPriQueueValueError("in pop")
        return self._elems[-1]
    
    # 弹出最高优先级O(1)
    def dequeue(self):
        if self.is_empty():
            raise ListPriQueueValueError("in pop")
        return self._elems.pop()
    
    # 入队新的优先级O(n)
    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] < e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

if __name__=="__main__":
    l = List_Pri_Queue([4, 6, 1, 3, 9, 7, 2, 8])
    print(l._elems)
    print(l.peek())
    l.dequeue()
    print(l._elems)
    l.enqueue(5)
    print(l._elems)
    l.enqueue(1)
    print(l._elems)
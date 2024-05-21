class Deque:
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        """从队头加入一个元素"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """从队尾加入一个元素"""
        self.items.append(item)

    def remove_front(self):
        """从队头删除一个元素"""
        return self.items.pop(0)
    
    def remove_rear(self):
        """从队尾删除一个元素"""
        return self.items.pop()
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []
    
    def size(self):
        """队列长度"""
        return len(self.items)
    
if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
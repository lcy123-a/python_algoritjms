class Node:
    def __init__(self, new_data):
        #链表有效负载 -- 数据
        self.data = new_data
        #链表指针
        self.next = None

    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class SingleCycleList:
    def __init__(self):
        self.head = None

    # 作头插入时2，需要先判断是否为空列表，需要注意插入顺序
    def add(self, item):
        # 因为实现单链表时， 可以统一方式作头插入，所以需要三行代码
        # 而作双向链表和循环链表时，要区别是否为空链表，所以插入的代码就变化了很多。（简单一行，复杂多行）
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.set_next(self.head)
        else:
            node.set_next(self.head)
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(node)
            self.head = node

    # 作尾插入时，需要先判断是否为空列表
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.set_next(self.head)
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(node)
            node.set_next(self.head)

    # 指定位置插入节点
    def insert(self, pos, item):
        # 相当于头插入
        if pos <= 0:
            self.add(item)
        # 相当于尾插入
        elif pos >= self.size():
            self.append(item)
        else:
            node = Node(item)
            current = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                current = current.get_next()
            node.set_next(current.get_next())
            current.set_next(node)

    # 删除指定节点数据
    def remove(self, item):
        if self.is_empty():
            return
        previous = None
        current = self.head
        while current.get_next() != self.head:
            # 待删除节点如果找到
            if current.get_data() == item:
                if current == self.head:
                    rear = self.head
                    while rear.get_next() != self.head:
                        rear = self.head
                        while rear.get_next() != self.head:
                            rear = rear.get_next()
                        self.head = current.get_next()
                        rear.set_next(self.head)
                else:
                    previous.set_next(current.get_next())
                return
            else:
                previous = current
                current = current.get_next()
        if current.get_data() == item:
            if current == self.head:
                self.head = None
                return
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        while current.get_next() != self.head:
            if current.get_data() == item:
                found = True
            current = current.get_next()
        return found
    
    def is_empty(self):
        return self.head == None
    
    def __len__(self):
        return self.size()
    
    def size(self):
        if self.is_empty():
            return 0
        count = 0
        current = self.head
        while current.get_next() != self.head:
            count += 1
            current = current.get_next()
        return count
    
    def show(self):
        if self.is_empty():
            return
        current = self.head
        print(current.get_data(), end=' ')
        while current.get_next() != self.head:
            current = current.get_next()
            print(current.get_data(), end=' ')
        print()

if __name__ == '__main__':
    s_list = SingleCycleList()
    print(s_list.is_empty())
    s_list.add(5)
    s_list.add(4)
    s_list.add(76)
    s_list.add(23)
    s_list.show()
    s_list.append(47)
    s_list.show()
    s_list.insert(0, 100)
    s_list.show()
    s_list.insert(99, 345)
    s_list.show()
    s_list.insert(3, 222)
    s_list.show()
    s_list.remove(76)
    s_list.show()
    print(s_list.search(23))
    s_list.show()
    print(s_list.is_empty())
    print(s_list.size())
    print(len(s_list))
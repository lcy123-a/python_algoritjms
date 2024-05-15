# 单向链表

class SingleNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self, data = None):
        node = SingleNode(data)
        self._head = node if node.data else None

    def is_empty(self):
        return self._head == None
    
    def length(self):
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.next
        return count
    
    # 头部添加元素
    def add(self, data):
        node = SingleNode(data)
        node.next = self._head
        self._head = node

    # 尾部添加元素
    def append(self, data):
        node = SingleNode(data)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    # 指定位置插入
    def insert(self, pos, data):
        node = SingleNode(data)
        cur = self._head
        count = 0
        if self.length() >= pos >= 0:
            while cur:
                if count + 1 == pos:
                    node.next = cur.next
                    cur.next = node
                    break
                # pos为0
                elif count == pos:
                    self.add(data)
                    break
                count += 1
                cur = cur.next
        elif pos < 0:
            self.add(data)
        else:
            self.append(data)
        # 如果列表中插入时没有元素
        if not self._head:
            self.append(data)

    # 遍历
    def travel(self):
        cur = self._head
        while cur:
            print(cur.data)
            cur = cur.next

    # 移除出现的第一个元素
    def remove(self, data):
        if self.is_empty():
            return
        node = self.__find(data)
        cur = self._head
        while cur:
            # 如果要移除的元素是头节点
            if cur.data == node.data:
                self._head = cur.next
                break
            elif cur.next.data == node.data:
                cur.next = node.next
                break
            cur = cur.next

    # 私有方法，用于查找节点
    def __find(self, data):
        cur = self._head
        node = SingleNode(data)
        while cur:
            if cur.data == node.data:
                return cur
            cur = cur.next
        return node
    
    # 查找，找不到返回-1,找到则返回索引
    def search(self, data):
        index = -1
        cur = self._head
        count = 0
        while cur:
            if cur.data == data:
                index = count
                break
            count += 1
            cur = cur.next
        return index
    
def main():
    ssl = SingleLinkedList()
    print(ssl.is_empty())
    print(ssl.length())
    ssl.append(1)
    ssl.append(100)
    ssl.append(2)
    ssl.append(200)
    print(ssl.is_empty)
    print(ssl.length())

    print("*" * 50)
    ssl.travel()
    ssl.add(100)
    ssl.travel()
    ssl.insert(-1, "sss")
    ssl.travel()
    print("*" * 50)
    print(ssl.search("sss"))
    print("*" * 50)
    ssl.remove(100)
    ssl.travel()

if __name__ == '__main__':
    main()
# 在链表中增加功能

class Node(object):
    # 节点类
    def __init__(self,item):
        self.item = item  # 记录数据
        self.next = None  # 记录下一个节点
        self.pre =  None  # 记录前面节点

class LList(object):
    def __init__(self):
        # 所有操作都是从头开始,需要记录头结点
        self.__head = None
 
    def is_empty(self):
        """链表是否为空"""
        return self.__head is None
 
    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
            # 定义计数器，遍历链表
        count = 1
        cur = self.__head
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count
 
    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
            # 定义游标，从头向尾移动
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.item, end=" ")
            # 让游标往后移动
            cur = cur.next
        # while循环会漏掉尾节点
        print(cur.item)
 
    def add(self,item):
        """链表头部添加元素"""
        # 创建新的节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
 
        # 遍历找到尾节点
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        # while 循环结束，cur指向尾节点
 
        # 新节点的next指向原来的头节点
        node.next = self.__head
        # 原来的头结点指向新节点
        self.__head = node
 
        # 让尾节点指向新的头
        cur.next = self.__head
        # 新的头结点指向尾节点
        self.__head.pre = cur
 
    def append(self,item):
        """"链表尾部添加元素"""
        # 判断链表是否为空
        if self.is_empty():
            self.add(item)
            return
 
        # 第一步,找尾节点
        cur = self.__head
        while cur.next is not self.__head:
            # 首节点的pre是尾节点
            cur = cur.next
        # while 循环结束,cur指向尾节点
        # 第二步,尾节点指向新节点
        node = Node(item)
        # 尾节点指向新的节点
        cur.next = node
        # 新的节点的pre指向原尾节点
        node.pre = cur
 
        # 新节点指向头节点
        node.next = self.__head
        # 头结点的pre指向新节点
        self.__head.pre = node
 
    def insert(self,pos, item):
        """指定位置添加元素"""
        if pos <=  0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 1 定义下标,与游标同步变化
            index = 0
            cur = self.__head
            while index < (pos - 1):
                index += 1
                cur = cur.next
            # 循环结束后,cur指向pos前置节点-
            node = Node(item)
            # 2、让新节点的next指向pos位置的节点
            node.next = cur.next
            # 让pos位置的节点的pre指向新节点
            cur.next.pre = node
            # 3、让pos位置的前置节点指向新节点
            cur.next = node
            # 让新节点的pre指向pos的前置节点
            node.pre = cur
 
    def remove(self,item):
        """删除节点"""
        if self.is_empty():
            return
            # 定义pre记录当前节点的前置节点
        pre = None
        cur = self.__head
        while cur.next is not self.__head:
            if cur.item == item:
                # 删除当前节点
                # 如果pre为空，删掉的是头 需要让尾节点指向新的头
                if pre is None:
                    # 找到尾节点
                    temp = self.__head
                    while temp.next is not self.__head:
                        temp = temp.next
                    # while循环结束，temp指向尾节点
                    # 头结点指向当前的下一个节点
                    self.__head = cur.next
                    # 当前的下一个节点指向头结点
                    cur.next.pre = self.__head
                    # 让尾节点指向新的头
                    temp.next = self.__head
                    # 新的头接点指向尾节点
                    self.__head.pre = temp
                else:
                    # 删除中间节点
                    # 上一个节点的next指向当前的的next即下一个节点
                    pre.next = cur.next
                    cur.next.pre = cur.pre
                return
            # pre 一直记录cur的前置节点
            pre = cur
            cur = cur.next
 
        # while循环处理不了尾节点，单独处理尾节点
        if cur.item == item:
            # 如果pre为空，证明当前只有一个节点，而且要删除这个节点
            if pre is None:
                self.__head = None
            else:
                # 让尾节点的前置节点指向头
                pre.next = self.__head
                self.__head.pre = cur.pre
 
    def search(self,item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
 
        cur = self.__head
        while cur.next is not self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        # 单独处理尾节点
        if cur.item == item:
            return True
        return False
    
    # 根据索引获得该位置的元素
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key < self.length():
            p = self.__head
            num = -1
            while p:
                num += 1
                if key == num:
                    return p.item
                else:
                    p = p.next
        else:
            raise IndexError
        
    # 判断两个列表是否相等 ==
    def __eq__(self, other):
        if self.length() == 0 and other.length() == 0:
            return True
        elif self.length() == other.length():
            for i in range(self.length()):
                if self[i] == other[i]:
                    pass
                else:
                    return False
            return True
        else:
            return False
        
    # 判断两个列表是否不相等
    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True
        
    # >
    def __gt__(self, other):
        l1 = self.length()
        l2 = other.length()
        if not isinstance(other, LList):
            raise TypeError
        if l1 == l2:
            for i in range(l1):
                if self.__getitem__(i) == other.__getitem__(i):
                    continue
                elif self.__getitem__(i) < other.__getitem__(i):
                    return False
                else:
                    return True
            return False
        if l1 > l2:
            for i in range(l2):
                if self.__getitem__(i) == other.__getitem__(i):
                    continue
                elif self.__getitem__(i) < other.__getitem__(i):
                    return False
                else:
                    return True
            return True
        if l1 < l2:
            for i in range(l1):
                if self.__getitem__(i) == other.__getitem__(i):
                    continue
                elif self.__getitem__(i) > other.__getitem__(i):
                    return False
                else:
                    return True
            return False
    
    # <
    def __lt__(self, other):
        if self.__gt__(other) or self.__eq__(other):
            return False
        else:
            return True
    
    # >=
    def __ge__(self, other):
        if self.__eq__(other) or self.__gt__(other):
            return True
        else:
            return False
        
    # <=
    def __le__(self, other):
        if self.__eq__(other) or self.__lt__(other):
            return True
        else:
            return False
        
if __name__ == '__main__':
    mlist1 = LList()
    mList2 = LList()
    mlist1.append(1)
    mList2.append(1)
    mlist1.append(2)
    mList2.append(2)
    mList2.append(6)
    mList2.append(11)
    mList2.append(12)
    mList2.append(14)
    mlist1.travel()
    mList2.travel()
    print(mlist1.__eq__(mList2))
    print(mlist1.__ne__(mList2))
    print(mlist1.__le__(mList2))
    print(mList2.__getitem__(1))
    print(mlist1.__ne__(mList2))
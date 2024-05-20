# 异常类
class stringTypeError(TypeError):
    pass

# 节点类
class Node(object):
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

# 单链表类
class single_list(object):
    def __init__(self):
        self._head = None
        self._num = 0

    def __len__(self):
        return self._num
    
    def prepend(self, elem):
        self._head = Node(elem, self._head)
        self._num += 1

    def append(self, elem):
        if self._head is None:
            self._head = Node(elem)
            self._num += 1
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = Node(elem)
        self._num += 1

    def pop_last(self):
        if self._head is None:
            raise ValueError("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self._num -= 1
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._num -= 1
        return e
    
    def delitem(self, key):
        if key == len(self) - 1:
            self.pop_last()
        elif 0 <= key < len(self) - 1:
            p = self._head
            pre = None
            num = -1
            while p is not None:
                num += 1
                if num == key:
                    if not pre:
                        self._head = p.next
                        self._num -= 1
                    else:
                        pre.next = p.next
                        self._num -= 1
                    break
                else:
                    pre = p
                    p = p.next
        else:
            raise IndexError
        

    def insert(self, key, elem):
        if key >= len(self) - 1:
            self.append(elem)
        elif 0 <= key < len(self) - 1:
            p = self._head
            pre = None
            num = -1
            while p:
                num += 1
                if num == key:
                    if not pre:
                        self._head = Node(elem, self._head)
                        self._num += 1
                    else:
                        pre.next = Node(elem, pre.next)
                        self._num += 1
                    break
                else:
                    pre = p
                    p = p.next
        else:
            raise IndexError
        
    # 打印显示
    def printall(self):
        p = self._head
        while p:
            print(p.elem, end="")
            if p.next:
                print(", ", end="")
            p = p.next
        print("")


#单链表字符串类
class string(single_list):
    def __init__(self, value):
        self.value = str(value)
        single_list.__init__(self)
        for i in range(len(self.value)-1,-1,-1):
            self.prepend(self.value[i])

    def length(self):
        return self._num

    #获取字符串对象值的列表，方便下面使用
    def get_value_list(self):
        l = []
        p = self._head
        while p:
            l.append(p.elem)
            p = p.next
        return l

    def printall(self):
        p = self._head
        print("字符串结构：",end="")
        while p:
            print(p.elem, end="")
            if p.next:
                print("-->", end="")
            p = p.next
        print("")

    #朴素的串匹配算法，返回匹配的起始位置
    def naive_matching(self, p):  #self为目标字符串，t为要查找的字符串
        if not isinstance(self, string) and not isinstance(p, string):
            raise stringTypeError
        m, n = p.length(), self.length()
        i, j = 0, 0
        while i < m and j < n:
            if p.get_value_list()[i] == self.get_value_list()[j]:#字符相同，考虑下一对字符
                i, j = i+1, j+1
            else:               #字符不同，考虑t中下一个位置
                i, j = 0, j-i+1
        if i == m:              #i==m说明找到匹配,返回其下标
            return j-i
        return -1

    #kmp匹配算法，返回匹配的起始位置
    def matching_KMP(self, p):
        j, i = 0, 0
        n, m = self.length(), p.length()
        while j < n and i < m:
            if i == -1 or self.get_value_list()[j] == p.get_value_list()[i]:
                j, i = j + 1, i + 1
            else:
                i = string.gen_next(p)[i]
        if i == m:
            return j - i
        return -1

    # 生成pnext表
    @staticmethod
    def gen_next(p):
        i, k, m = 0, -1, p.length()
        pnext = [-1] * m
        while i < m - 1:
            if k == -1 or p.get_value_list()[i] == p.get_value_list()[k]:
                i, k = i + 1, k + 1
                pnext[i] = k
            else:
                k = pnext[k]
        return pnext

    #把old字符串出现的位置换成new字符串
    def replace(self, old, new):
        if not isinstance(self, string) and not isinstance(old, string) \
                and not isinstance(new, string):
            raise stringTypeError

        while self.matching_KMP(old) >= 0:
            #删除匹配的旧字符串
            start = self.matching_KMP(old)
            print("依次发现的位置:",start)
            for i in range(old.length()):
                self.delitem(start)
            #末尾情况下时append追加的，顺序为正；而前面的地方插入为前插；所以要分情况
            if start<self.length():
                for i in range(new.length()-1, -1, -1):
                    self.insert(start,new.value[i])
            else:
                for i in range(new.length()):
                    self.insert(start,new.value[i])



if __name__=="__main__":

    a = string("abc")
    print("字符串长度：",a.length())
    a.printall()
    b = string("abcbccdabc")
    print("字符串长度：", b.length())
    b.printall()
    print("朴素算法_匹配的起始位置：",b.naive_matching(a),end=" ")
    print("KMP算法_匹配的起始位置：",b.matching_KMP(a))
    c = string("xu")
    print("==")
    b.replace(a,c)
    print("替换后的字符串是：")
    b.printall()
    print(b.get_value_list())
class Lnode(object):
    def __init__(self, last):
        self.data = [None for i in range(100)]
        self.last = last

def MakeEmpty(num):     # 初始化新的线性表
    PtrL = Lnode(num)
    return PtrL


def Find(x, L):         #  按值查找
    i = 0
    while (i <= L.last and L.data[i] != x):
        i += 1
        if (i > L.last):
            return -1
        else:
            return 1
        

def Insert(x, i, L):     # 插入新元素
    if i < 0 or i > L.last:
        print("位置不合理")
        return
    else:
        for j in range(L.last, i - 1, -1):
            L.data[j + 1] = L.data;
        L.data[i] = x
        L.last += 1
    return


def Delete(i, L):       # 删除操作
    if i < 0 or i >= L.last:
        print("不存在该元素")
        return
    else:
        for j in range(i, L.last - 1):
            L.data[j] = L.data[j + 1]
        L.last -= 1
        return
    



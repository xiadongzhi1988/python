#__author: Administrator
#data: 2019/05/25


class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
        print(self.items)
    def dequeue(self):
        l=self.items
        for i in l:
            print(i,end='')

q = Queue()
q.enqueue(1)
q.enqueue(4)
q.dequeue()



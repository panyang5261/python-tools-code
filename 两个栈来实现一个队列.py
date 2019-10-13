
# 题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

import copy

class Queue:

    def __init__(self):
        self.list_pop = []
        self.list_push = []

    def pop(self):
        if not self.list_pop:
            self.list_pop = copy.deepcopy(self.list_push[::-1])
            self.list_push = []

        if self.list_pop:
            return self.list_pop.pop()
        else:
            return None

    def push(self, v):
        self.list_push.append(v)


if __name__ == '__main__':
    q = Queue()
    q.push(123)
    q.push(444)
    print(q.pop())
    print(q.pop())
    print(q.pop())
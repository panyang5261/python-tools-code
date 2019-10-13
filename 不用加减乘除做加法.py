# 用“异或”和“或”操作实现整数加法运算：对应位数的“异或操作”可得到该位的数值，对应位的“与操作”可得到该位产生的高位进位，如：a=010010，b=100111，计算步骤如下：
#
# 第一轮：a^b=110101，(a&b)<<1=000100， 由于进位（000100）大于0，则进入下一轮计算，a=110101，b=000100，a^b=110001，(a&b)<<1=001000，由于进位大于0，则进入下一轮计算：a=110001，b=001000，a^b=111001，(a&b)<<1=0，进位为0，终止，计算结果为：111001。

def sum(a, b):
    while b:
        res = a ^ b
        b = (a & b) << 1
        a = res
    return a


def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i
import copy

g=test()
for n in [2,10]:
    g=(add(n,i) for i in g)
    # b = copy.deepcopy(g)
    # print(list(b))




if __name__ == '__main__':
    # print(sum(1, 3))
    # print(sum(3, 3))
    print(list(g))
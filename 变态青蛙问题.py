# (1) 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 理解为：f(n) = f(n-1) + f(n-2),往回推，到达N阶的时候，只有两种方式： 一次跳一个台阶和一次跳两个台阶,这两种方式是两个不同路径，
# 相加即可得到到N阶的总路径

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 两个问题思路一样。

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


#（2）一只青蛙一次可以跳上1级台阶，也可以跳上2 级……它也可以跳上n 级，此时该青蛙跳上一个n级的台阶总共有多少种跳法？
# 类似1中所属，N阶梯往回推，可以从 n-1,n-2,n-3....0开始跳到N阶。
# f(n) = f(n-1) + f(n-2) + ... + f(1) + f(0)
# f(n-1) = f(n-2) + ... + f(0)
# f(n) = 2 * f(n-1)
def steps(n):
    if n <= 1:
        return n

    return 2 * steps(n-1)

def steps2(n):
    f = 1
    for i in range(n-1):
        f = f * 2
    return f



if __name__ == '__main__':
    # print(fib(1), fib2(1))
    print(steps(3), steps2(0))
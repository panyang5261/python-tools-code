# 题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

def sum_n(n):
    if n<=1:
        return n
    return sum_n(n-1) + n


if __name__ == '__main__':
    print(sum_n(2))
# （5，12），（4，3），（7，10），（2，3），（6，6）。
# weight = [5,4,7,2,6]
# value = [12,3,10,3,6]
# tab = [0 for i in range(16)]
# for i in range(0, 5):
#     for j in range(weight[i], 16):
#         # print(j-weight[i], i, j)
#         tab[j] = max(tab[j-weight[i]]+value[i],tab[j])
#         print(tab[j])


import numpy as np

# 最小编辑距离
def eidt_solve(str_a, str_b):
    def diff(a, b):
        return not a == b

    res_arr = np.zeros((len(str_a)+1, len(str_b)+1), dtype=np.int32)
    for i in range(1, len(str_a)+1):
        res_arr[i, 0] = i
    for i in range(1, len(str_b)+1):
        res_arr[0, i] = i
    for a in range(1, len(str_a)+1):
        for b in range(1, len(str_b)+1):
            res_arr[a, b] = min(res_arr[a-1, b-1]+diff(str_b[b-1], str_a[a-1]), res_arr[a-1, b]+1,res_arr[a, b-1]+1)
            print(res_arr[a, b])
    return res_arr[-1, -1]



def solve(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength+1, totalWeight+1), dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(1, totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1]


def solve2(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalWeight)+1, dtype=np.int32)
    for i in range(1, totalLength+1):
        for j in range(totalWeight,0,-1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
            print(resArr[j])
        print('---------')
    return resArr[-1]


def solve3(vlist,wlist,totalWeight,totalLength):
    """完全背包问题"""
    resArr = np.zeros((totalWeight)+1,dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
                print(resArr[j])
        print('---------')
    return resArr[-1]


if __name__ == '__main__':
    # v = [0,60,100,120]
    # w = [0,10,20,30]
    # v = [0, 10, 5, 4, 3, 2, 1]
    # w =[0, 1,2,3,4,5]
    v = [0, 5,7]
    w = [0, 5,8]
    weight = 10
    n = 2
    result = solve2(v,w,weight,n)

    # result = eidt_solve('exponential', 'polynomial')

    print(result)

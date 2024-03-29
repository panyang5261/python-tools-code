# 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字
# 例子说明：
# 如输入一个长度为 9 的数组｛ 1, 2, 3, 2, 2, 2, 5, 4, 2｝。由于数字 2 在数组中出现了 5 次，超过数组长度的一半，因此输出 2 。
#


def get_half_num(nums:list):
    count = 0
    res = None
    for num in nums:
        if count == 0:
            res = num
        if num == res:
            count += 1
        else:
            count -= 1

    if res:
        count = 0
        for num in nums:
            if num == res:
                count += 1
        return res if count >= len(nums) // 2 else None
    return res


if __name__ == '__main__':
    print(get_half_num([11,22,11,55,11,66,11]))
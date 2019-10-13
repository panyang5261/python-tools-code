
def merge_list(la, lb):
    a = b = 0
    new_list = []
    while(a < len(la) and b < len(lb)):
        if la[a] < lb[b]:
            value = la[a]
            a += 1
        else:
            value = lb[b]
            b += 1
        new_list.append(value)

    if a < len(la):
        new_list.extend(la[a:])

    if b < len(lb):
        new_list.extend(lb[b:])
    return new_list


la = [1,3,5,6]
lb = [2,4,6,8]

print(merge_list(la, lb))
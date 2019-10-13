

def num_to_binary(n):
    binary = ''
    while n:
        b = n % 2
        n = n // 2
        binary = str(b) + binary

    if not len(binary) == 8:
        binary = ''.join(['0' for _ in range(8-len(binary))]) + binary
    return binary


def binary_to_int(binary):
    value = 0
    for n, b in enumerate(binary):
         value += int(b) * (2 ** (len(binary)-n-1))
    return value


if __name__ == '__main__':
    b = num_to_binary(4)
    i = binary_to_int(b)
    print(b, i)


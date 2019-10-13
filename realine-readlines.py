

with open('./README.MD', 'r+') as f:
    lines = f.readlines()
    print(type(lines))
    print(lines)

    line = f.readline()
    print(type(line))
    print(line)
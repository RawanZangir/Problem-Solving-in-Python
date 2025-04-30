def pyramid(size):
    pyramid = []
    row = [' '] * size

    for i in range(size):
        row.pop(0)
        row.append('*')
        pyramid.append(row.copy())
        print(row)

    return pyramid

x = 5
result = pyramid(x)

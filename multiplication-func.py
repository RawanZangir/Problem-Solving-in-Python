def multiplication(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        table.append(row)
    return table

x = int(input("Enter a number: "))
print(multiplication(x))



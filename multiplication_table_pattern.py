# Display a multiplication table up to 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}")
        
# Create a list of lists for a multiplication table

x = int(input("Enter a number "))
table = [] 

for i in range(1, x+1):
    y = []  
    for j in range(1, x+1):
        if j <= i:
            y.append(i * j)
        else:
            break
    table.append(y)

print(table)



     




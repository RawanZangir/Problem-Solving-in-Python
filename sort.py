# Take 5 numbers from the user and display them sorted in ascending and descending order

y = []
print("Enter 5 numbers")
for i in range(5):
    num = input("Enter a number")
    y.append(num)
    

ascending = sorted(y)
descending = sorted(y, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)


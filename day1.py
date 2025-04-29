x = "Welcome to python"
count = 0

for i in range(len(x)):
    if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        count += 1

print("Number of vowels=", count)

############################


for i in range(1, 6):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}")
     
##################################

x = 6

for i in range(1, x + 1):
 
 print(' ' * (x - i) + '*' * i)
    








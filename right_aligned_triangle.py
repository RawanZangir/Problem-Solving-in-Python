# Print a right-aligned triangle pattern using asterisks

x = 6
for i in range(1, x + 1):
 
 print(' ' * (x - i) + '*' * i)
 
# A right-aligned triangle pattern using asterisks with lists   
x = 5
pyramid = []
row = [' '] * x  

for i in range(x):
    row.pop(0)        
    row.append('*')   
    print(row)

   

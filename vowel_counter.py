# Count the number of vowels (a, e, i, o, u) in a given string

x = "Welcome to python"
count = 0

for i in range(len(x)):
    if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        count += 1

print("Number of vowels=", count)

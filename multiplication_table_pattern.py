# Display a triangle-style multiplication table up to 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}")

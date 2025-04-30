def sort():
    numbers = []
    print("Enter 5 numbers:")
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))  
        numbers.append(num)
    
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    
    return ascending, descending


ascending, descending = sort()
print("Ascending order:", ascending)
print("Descending order:", descending)


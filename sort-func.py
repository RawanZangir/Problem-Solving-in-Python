def sort():
    numbers = []
    print("Enter 5 numbers:")
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)

    return ascending, descending

if __name__ == "__main__":
    ascending, descending = sort()
    print("Ascending:", ascending)
    print("Descending:", descending)

while True:
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Please try again.")
    elif name.isdigit():
        print("Name cannot be a number. Please enter a valid name.")
    else:
        break

while True:
    email = input("Enter your email: ").strip()
    
    if "@" not in email or "." not in email:
        print("Invalid email: must contain '@' and '.'")
    elif email.index("@") > email.index("."):
        print("Invalid email: '.' must appear after '@'")
    else:
        break

print(f"\nYour data:\nName: {name}\nEmail: {email}")

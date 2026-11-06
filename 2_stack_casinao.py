# Assessment 3.2 - Stack (LIFO) | Last Name: CASINAO

def main():
    name = input("Enter your last name [CASINAO]: ").strip().upper() or "CASINAO"
    stack = []

    print("\nPUSHING LETTERS")
    for letter in name:
        stack.append(letter)
        print("Pushed:", letter, "| Stack:", stack)

    print("\nPOPPING LETTERS")
    while stack:
        removed = stack.pop()
        print("Popped:", removed, "| Stack:", stack)

    print("\nThe stack is now empty.")

if __name__ == "__main__":
    main()

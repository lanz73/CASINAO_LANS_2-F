# Assessment 3.2 - Array | Last Name: CASINAO

def main():
    name = input("Enter your last name [CASINAO]: ").strip().upper() or "CASINAO"
    letters = []

    print("\nADDING LETTERS")
    for letter in name:
        letters.append(letter)
        print("Added:", letter, "| Array:", letters)

    print("\nREMOVING LETTERS")
    while letters:
        removed = letters.pop(0)
        print("Removed:", removed, "| Array:", letters)

    print("\nThe array is now empty.")

if __name__ == "__main__":
    main()

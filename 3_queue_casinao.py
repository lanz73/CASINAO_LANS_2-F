# Assessment 3.2 - Queue (FIFO) | Last Name: CASINAO

from collections import deque

def main():
    name = input("Enter your last name [CASINAO]: ").strip().upper() or "CASINAO"
    queue = deque()

    print("\nENQUEUING LETTERS")
    for letter in name:
        queue.append(letter)
        print("Enqueued:", letter, "| Queue:", list(queue))

    print("\nDEQUEUING LETTERS")
    while queue:
        removed = queue.popleft()
        print("Dequeued:", removed, "| Queue:", list(queue))

    print("\nThe queue is now empty.")

if __name__ == "__main__":
    main()

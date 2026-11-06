# Assessment 3.2 - Linked List | Last Name: CASINAO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_first(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return " -> ".join(items) if items else "Empty"

def main():
    name = input("Enter your last name [CASINAO]: ").strip().upper() or "CASINAO"
    linked_list = LinkedList()

    print("\nADDING LETTERS")
    for letter in name:
        linked_list.append(letter)
        print("Added:", letter, "| Linked List:", linked_list.display())

    print("\nREMOVING LETTERS")
    while linked_list.head is not None:
        removed = linked_list.remove_first()
        print("Removed:", removed, "| Linked List:", linked_list.display())

    print("\nThe linked list is now empty.")

if __name__ == "__main__":
    main()

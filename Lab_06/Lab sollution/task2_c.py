class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_reversed(head):
    if head is None:
        return
    else:
        print_reversed(head.next)
        print(head.value)

# Test the function
# Create the linked list: 10 -> 20 -> 30 -> 40
head = SinglyNode(10)
head.next = SinglyNode(20)
head.next.next = SinglyNode(30)
head.next.next.next = SinglyNode(40)

print("Printing the linked list in reversed order:")
print_reversed(head)

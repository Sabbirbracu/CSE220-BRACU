class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def recursive_sum(head):
    if head is None:
        return 0
    else:
        return head.value + recursive_sum(head.next)

# Test the function
# Create the linked list: 1 -> 2 -> 3 -> 4
head = SinglyNode(1)
head.next = SinglyNode(2)
head.next.next = SinglyNode(3)
head.next.next.next = SinglyNode(4)

total_sum = recursive_sum(head)
print(f"The sum of all elements in the linked list is: {total_sum}")

"""
Solving using two pointers for removing duplicates from an unsorted linked list

- two pointers: current (iterates through the list for each node) and
- runner (pointer checks all subsequent nodes to see if any duplicates exist).
- If a duplicate is found, runner pointer skips it by adjusting the next
  pointer of the previous node.
- repeat until the end of the list.
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    current = head
    
    while current:
        runner = current
        
        # Check all subsequent nodes for duplicates
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        current = current.next
    
    return head


# Example usage:
# Create a linked list: 1 -> 5 -> 2 -> 2 -> 6 -> 6 -> None
head = ListNode(1)
head.next = ListNode(5)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(6)

print("Original linked list:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

head = remove_duplicates(head)

print("Linked list after removing duplicates:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")


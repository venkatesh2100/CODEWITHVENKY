# Definition for singly-linked list.
class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenlist(self, head: listNode) -> listNode:
        if not head or not head.next:
            return head  # If the list is empty or has only one node, return it

        # Initialize pointers for odd and even lists
        odd = head
        even = head.next
        even_head = even  # Save the head of the even list

        # Rearrange nodes
        while even and even.next:
            odd.next = even.next  # Link the next odd node
            odd = odd.next        # Move odd pointer forward
            even.next = odd.next  # Link the next even node
            even = even.next      # Move even pointer forward

        # Combine the odd and even lists
        odd.next = even_head
        return head

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = listNode(values[0])
    current = head
    for val in values[1:]:
        current.next = listNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Test the solution
head = create_linked_list([1, 2, 3, 4, 5])
solution = Solution()
result = solution.oddEvenlist(head)
print_linked_list(result)

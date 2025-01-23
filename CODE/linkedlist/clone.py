
# Node class to represent
# elements in the linked list
class Node:
    def __init__(self, x, nextNode=None, randomNode=None):
        # Data stored in the node
        self.data = x
        # Pointer to the next node
        self.next = nextNode
        # Pointer to a random
        # node in the list
        self.random = randomNode


# Function to clone the linked list
def cloneLL(head):
    temp = head
    # Create a dictionary to map original
    # nodes to their corresponding copied nodes
    mpp = {}

    # Step 1: Create copies of each node
    # and store them in the map
    while temp is not None:
        # Create a new node with the
        # same data as the original node
        newNode = Node(temp.data)
        # Map the original node to its
        # corresponding copied node in the dictionary
        mpp[temp] = newNode
        # Move to the next node in the original list
        temp = temp.next

    temp = head
    # Step 2: Connect the next and random
    # pointers of the copied nodes using the dictionary
    while temp is not None:
        # Access the copied node corresponding
        # to the current original node
        copyNode = mpp[temp]
        # Set the next pointer of the copied node
        # to the copied node mapped to the
        # next node in the original list
        copyNode.next = mpp[temp.next]
        # Set the random pointer of the copied node
        # to the copied node mapped to the
        # random node in the original list
        copyNode.random = mpp[temp.random]
        # Move to the next node
        # in the original list
        temp = temp.next

    # Return the head of the
    # deep copied list from the dictionary
    return mpp[head]


# Function to print the cloned linked list
def printClonedLinkedlist(head):
    while head is not None:
        print(f"Data: {head.data}", end="")
        if head.random is not None:
            print(f", Random: {head.random.data}")
        else:
            print(", Random: nullptr")
        head = head.next


# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked list with Random Pointers:")
    printClonedLinkedlist(head)

    # Clone the linked list
    clonedlist = cloneLL(head)

    print("\nCloned Linked list with Random Pointers:")
    printClonedLinkedlist(clonedlist)

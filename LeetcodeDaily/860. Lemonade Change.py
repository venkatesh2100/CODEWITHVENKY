from collections import deque

class Solution:
    def lemonadeChange(self, bills) -> bool:
        change = deque()  # Initialize the deque to store change
        for i in bills:
            if not self.paybill(change, i):  # Process each bill
                return False  # If unable to give correct change, return False
        return True  # Successfully processed all transactions

    def paybill(self, change, order) -> bool:
        if order == 5:
            change.append(5)  # Add a $5 bill to the change pool
            return True

        order -= 5  # Deduct the cost of the lemonade ($5)
        while order > 0 and change:  # Try to give change
            val = change.pop()  # Take the largest available bill
            if val <= order:
                order -= val  # Reduce the remaining change needed
            else:
                change.append(val)  # Restore bill to the deque if it’s too large

        if order > 0:  # If we couldn't provide exact change
            return False

        change.append(5)  # Add the $5 bill from the current transaction
        return True

# Test the function
bill = [5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20]
a = Solution()
print(a.lemonadeChange(bill))  # Expected: True

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        num2_bits = bin(num2).count('1')
        print(num2_bits)
        x = 0
        for i in range(31, -1, -1):
            if num1 & (1 << i):
                if num2_bits > 0:
                    x+= (1 << i)
                    num2_bits -= 1


        for i in range(32):
            if num2_bits == 0:
                break
            if not (x & (1 << i)):
                x ``= (1 << i)
                num2_bits -= 1

        return x

num1 = 3
num2 = 5
solution = Solution()
result = solution.minimizeXor(num1, num2)
print(f"The integer x that minimizes XOR is: {result}")
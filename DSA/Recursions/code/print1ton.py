#XXX : print 1 to n 
#TODO: Induction Hypothesis
def func1ton(n):
    if n==1:
        print(1)
        return 

    func1ton(n-1)
    print(n)

# func1ton(10)
#TODO: Print N time Name
def name1t0n(i , n):
    if n < i:
        print("Venky")
        return
    name1t0n(i+1 , n)
    print("Venky")
# name1t0n(0,10)
#
#TODO:Sum of First N numbers
def sumNum(sumi,n):
    if n == 1:
        return sumi+1
    sumi+=n
    return sumNum(sumi,n-1)

print(f'Paramatric Recursion:',sumNum(0,3))
def funcSum(n):
    if n == 0:
        return 0 
    return n + funcSum(n-1)
print(f'Functional Recursion N:',funcSum(10))
#TODO: Factorial Using Recursion
def Factorial(n):
    if n == 1:
        return 1 
    return n * Factorial(n-1)
print(f'Factorial N:',Factorial(4))
#TODO: Two pointer Reverse
def TwopointerReverse(arr):
    size = len(arr)
    left = 0 
    right = size -1 
    while left < right:
        temp = arr[left]
        arr[left] =arr[right]
        arr[right] = temp
        left+=1 
        right-=1 
    return arr
print(f'Two Pointer Reverse Array:',TwopointerReverse([2,3,5,343,2,432,424,2,34,234]))
#HACK: Using Recursion Reverse
def ReveserRecursion(l , r ,arr):
    if l >= r :
        return arr
    arr[l] , arr[r] = arr[r] , arr[l]
    return ReveserRecursion(l+1,r-1 ,arr)
print(f'Recursion Reverse:',ReveserRecursion(0,10,[23,34545,34,5,34,64564,56,5464,23,2,53,]))
#TODO: Palindrome Recursion 
def Palindrome(l,r,s):
    if l >=r:
        return True
    if s[l]!=s[r]:
        return False
    return Palindrome(l+1,r-1,s)
print(f'Recursion Palindrome',Palindrome(0,5,'abccba'))
#TODO: Recursion DP Fibbnoci
def DPfibba(n, DP):
    if n in DP:
        return DP[n]
    if n == 1:
        return 1 
    if n == 0:
        return 0 
    DP[n]=DPfibba(n-1,DP) + DPfibba(n-2,DP)
    return DP[n]
print(f'Fibbnoci number',DPfibba(10,DP={}))

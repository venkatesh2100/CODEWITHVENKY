import time
def extraLongFactorials(n):
    # Write your code here
    ##?Method One
    tot=1
    for i in range(1,n+1):
      # print(i)
      tot*=i
    return tot

    # return tot
    ##?Methid 2 using Recursion
    # if n==0 or n==1:
    #   return 1
    # return n*extraLongFactorials(n-1)


itime=time.time()
print(extraLongFactorials(900))

print(time.time()-itime)
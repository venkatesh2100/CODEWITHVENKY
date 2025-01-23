import time

def fibano(n,arr=None):
  if arr==None:
    arr=[-1]*(n+1)
  if n==0:
    return 0
  if n==1:
    return 1
  if arr[n]!=-1:
    return n
  arr[n]=fibano(n-1,arr)+fibano(n-2,arr)
  return arr[n]


  for i in range(2,n+1):
    arr


itime=time.time()
print(fibano(3))
print(f'{time.time()-itime:.6f}')

t=int(input())

for i in range(t):
  a ,b ,c =map(int,input().split())
  avg=(a+b)/2
  if avg > c:
    print("YES")
  else:
    print("NO")
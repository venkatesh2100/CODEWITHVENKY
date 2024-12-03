import string
from collections import Counter
dict={1:'c',2:'d',3:'v'}
dict.pop(2)

dict.setdefault(4,'b')
# dict.clear()
print(dict.keys())
newd=dict.copy()
for i,val in newd.items():
  print(i , val)
print(dict)
print(newd)


d={}
ds={}
s="ksnfkfjsdfklsdlkfklsdfjlksflskndf"

# ds=Counter(s)
# print(ds)
for i in s:
  ds[i]=ds.get(i,0)+1
print(ds)
print(ds)


# arr=[]
# for f,x in ds.items():
#   arr.append([f]*x)
# print(arr)

# newval=[(x for x in s)]

# print(type(val))
# print(newval)

# # key=(x for x in range(val))
# print(key)
# d=d.fromkeys(key,val)
# print(d)
# print(val)
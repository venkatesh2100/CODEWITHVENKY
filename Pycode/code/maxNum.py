list=[10 ,30 , 40 ,50 ,1]
list.append(999)
smallNum=list[0]
largeNum=list[0]
list.insert(1,3)
# print(name=list)
# print(name=list.sort())
print(list.reverse())
for i in list:
  if smallNum > i:
    smallNum=i
  if largeNum < i:
    largeNum=i
print(smallNum)
print(largeNum)

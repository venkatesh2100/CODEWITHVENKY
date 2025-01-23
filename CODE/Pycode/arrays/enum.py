mark=[2,3,4,5]
target=7

def Twosum(arr,target):
    #hashmap
    numMap={}

    for index,num in enumerate(arr):
        comp=target-num
        if comp in numMap:
            return [numMap[comp],index]
        numMap[num]=index

print(Twosum(mark,target))

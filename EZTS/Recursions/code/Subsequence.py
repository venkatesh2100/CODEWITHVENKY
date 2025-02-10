 #TODO: Generate a Subsquence Recursion  Tree.

from typing import List


def Subsquence(i:int,res:List[int],arr:List[int] )->None:
    if i == len(arr):
        print(res)
        return
    res.append(arr[i])
    Subsquence(i+1,res,arr)
    # print("Print the Next Half")
    res.pop()
    Subsquence(i+1,res ,arr)
arr = [1,2,3 ,3,4,5,5,32,5,]
print(Subsquence(1,[],arr))

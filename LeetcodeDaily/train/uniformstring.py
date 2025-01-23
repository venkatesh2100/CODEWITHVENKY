

def weightedUniformStrings(s,queries):
    # Write your code here
    dt={}
    # dt=Counter(s)

    for i in s:
        dt[i]=dt.get(i,0)+1
    print(dt)
    arr=set()

    for k,val in dt.items():
        for x in range(1,val+1):
            arr.add((x*(ord(k)-ord('a')+1)))

            # print((x*(ord(k)-ord('a')+1)))
    print(arr)
    # for k,val in dt.items():
    #     arr.append((val*(ord(k)-ord('a')+1)))
    res=[]
    print(queries)
    for i in queries:
        if i in arr:
            res.append("Yes")
        else:
            res.append("No")
    return res
    # for i in range(len(arr)):
    #     if arr[i]>queries[i]:
    #         print("NO")
    #     else:
    #         print("YES")

    # print(arr)


print(weightedUniformStrings("bbbaa",[2,4,6,1]))


def weightedUniformStrings(s, queries):
    # Calculate uniform substring weights
    uniform_weights = set()
    prev_char = ''
    count = 0

    for char in s:
        if char == prev_char:
            count += 1
        else:
            count = 1
        uniform_weights.add(count * (ord(char) - ord('a') + 1))
        prev_char = char

    # Process queries
    result = ["Yes" if query in uniform_weights else "No" for query in queries]
    return result

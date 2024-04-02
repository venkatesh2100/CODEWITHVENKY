def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    pass
    union=[]
    n=len(a)
    m=len(b)
    i=0
    j=0
    while i<n and j<m:
      if a[i] < b[j]:
        union.append(a[i])
        i=i+1
      elif a[i] > b[j]:
        union.append(b[j])
        j=j+1
      else:
        union.append(a[i])
        i=i+1
        j=j+1
        
    
    while i<n:
      union.append(a[i])
      i=i+1
    while j<m:
      union.append(b[i])
      j=j+1
    
    union=sorted(set(union))
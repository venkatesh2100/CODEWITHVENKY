n=int(input("Enter the Number:"))
for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
            #by this way we can generate the code 
            print(i,'is equal',j,'*',i//j )
            break
    else:
        print(i)



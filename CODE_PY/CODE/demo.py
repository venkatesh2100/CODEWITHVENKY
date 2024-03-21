print(200000*2)
List=[1,2,3,4,5,6,7,8,9]
List.append(3993)
print(List)
rba=['red','green','yellow']
rbga=rba
print(id(rba)==id(rbga))
print(rba[1])
print(len(rbga))
print(rba[:])
x=int(input("Enter the first number:"))
if(x>0):
    print("The number is greater than 0")
elif(x<0):
    print("The number is less 0")
elif(x==0):
    print("The number is equal to zero")
for i in range(x):
    print(i)

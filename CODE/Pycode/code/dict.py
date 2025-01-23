# disct={
#   "name":"venky",
#   "car":"volvo"
# }
# print(len(disct))
# print(type(disct))

# name=input("Enter your name")
# print(name +" moron")
# age=30
# formatted=f"hello{name} is {age:.2f}"
# print(formatted)

# print(name.upper())
s=input("Enter your response")

if s in ["y","yes"]:
  print("agrees")
else:
  print("nope")

scores=[432,32,32,3,2,3,323]
# average=sum(scores)/len(scores)
scores.append(10000)
def average():
  average=sum(scores)/len(scores)
  return average
print(f"{average():.2f}")

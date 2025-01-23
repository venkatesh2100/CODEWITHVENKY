str="A man, a plan, a canal: Panama"

res=''.join(char for char in str if char.isalnum()).lower()
print(res)


for char in str:
    print(char)

s=[i.strip() for i in str if i.isalnum()]
print(s)

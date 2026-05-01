

n = int(input())
val = str(n)
bits = bin(n)[2:]
s = ''
print(bits)

mask = (1 << len(bits)) - 1
print(n ^ mask)
exit()
for i in bits:
    if i == '1':
        s+='0'
    else:
        s+='1'
val = int(s,2)
print(val)


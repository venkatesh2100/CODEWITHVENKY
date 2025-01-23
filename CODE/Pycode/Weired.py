

def algo(val):
    while val != 1:
        if val % 2 == 0:
            val //= 2
        else:
            val = (3 * val) + 1
        print(val)


# HACK: 421 LOOP LOL
val = int(input("Enter the Value:"))
algo(val)

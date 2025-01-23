

def split_and_join(line):
    # write your code here
    res=line.split(" ")

    val="-".join(res)
    return val
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
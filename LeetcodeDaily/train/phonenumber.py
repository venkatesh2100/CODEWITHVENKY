def process_input(input1):
    first = int(input1[0])
    res = ""
    # Determine initial state (E for even, O for odd)
    boo = "E" if first % 2 == 0 else "O"
    curr_count = first

    for i in range(1, len(input1)):
        if curr_count == 0:
            # Reset boo based on current digit
            boo = "E" if int(input1[i]) % 2 == 0 else "O"
            curr_count = int(input1[i])
        else:
            if boo == "O":  # Odd mode
                curr_count += int(input1[i])
                if curr_count % 2 == 0:  # If the sum becomes even
                    res += str(curr_count)
                    curr_count = 0
            else:  # Even mode
                curr_count += int(input1[i])
                if curr_count % 2 == 1:  # If the sum becomes odd
                    res += str(curr_count)
                    curr_count = 0


    # Add any remaining `curr_count` to `res` if it's non-zero
    if curr_count != 0:
        res += str(curr_count)

    return res


# Test the function
print(process_input("102938989"))  # Output

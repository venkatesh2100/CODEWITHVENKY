def prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum

def range_sum(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i-1]

# Example usage
arr = [10, 20, 30, 40, 50]
prefix_sum_arr = prefix_sum(arr)
print(range_sum(prefix_sum_arr, 2, 4))  # Output: 120
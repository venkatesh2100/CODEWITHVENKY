# sliding window Appraoch


def SlideMaxsum(arr):
    left = 0
    right = 0
    maxsum = float("-inf")
    window_sum = sum(arr[:right])
    for right in range(len(arr)):
        window_sum += arr[right]

        if window_sum < 0:
            window_sum = 0
            left = right + 1
        maxsum = max(window_sum, maxsum)
    return maxsum


arr = [10, 20, -10, 2, 3]

print(SlideMaxsum(arr))

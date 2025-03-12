

## sliding window Appraoch

def SlideMaxsum(arr):
    left = 0
    right = 0
    window_sum = sum(arr[:right])
    for right in range(len(arr)):
        window_sum =  arr[right]-arr[left]
        maxsum = max(window_sum,maxsum)
        left+=1
    return window_sum


arr = [10,20,-10,2,3]

print(SlideMaxsum(arr))

        

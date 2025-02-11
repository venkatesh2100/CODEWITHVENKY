class VenkySorting:

    def merge(self, arr, low, mid, high):
        left = arr[low:mid + 1]   # Left half
        right = arr[mid + 1:high + 1]  # Right half
        print(left)
        print(right)
        i = j = 0  # Pointers for left and right subarrays
        k = low  # Pointer for original array
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        
        mid = low + (high - low) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr, low, mid, high)


arr = [2, 10, 30, 1, 15, 3, 6]
ans = VenkySorting()
ans.mergeSort(arr, 0, len(arr) - 1)
print(arr)  # Sorted array output

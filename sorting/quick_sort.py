class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low + 1, high

        while True:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quick_sort(self, arr, low, high):
        while low < high:
            p_index = self.partition(arr, low, high)

            # Sort smaller partition first to optimize recursion
            if p_index - low < high - p_index:
                self.quick_sort(arr, low, p_index - 1)
                low = p_index + 1
            else:
                self.quick_sort(arr, p_index + 1, high)
                high = p_index - 1

arr = [1, 6, 3, 6, 8, 9]
low = 0
high = len(arr) - 1
sol = Solution()
sol.quick_sort(arr, low, high)
print(arr)  # Output the sorted array

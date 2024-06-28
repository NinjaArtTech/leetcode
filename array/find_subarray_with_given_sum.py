def find_subarray_with_given_sum(arr, n, s):
    left = 0
    current_sum = 0
    
    for right in range(n):
        # Add the rightmost element to the current_sum
        current_sum += arr[right]
        
        # While current_sum exceeds the target sum, move the left pointer to the right
        while current_sum > s and left <= right:
            current_sum -= arr[left]
            left += 1
        
        # Check if the current_sum is equal to the target sum
        if current_sum == s:
            return [left + 1, right + 1]  # Return 1-based indexing
        
    # If no subarray is found, return [-1]
    return [-1]

# Example usage:
arr = [1, 2, 3, 7, 5]
n = len(arr)
s = 12
print(find_subarray_with_given_sum(arr, n, s))  # Output should be [2, 4]

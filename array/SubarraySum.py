class Solution:
    def subarray_sum(nums, k):
        sum_map = {0: 1}  # Initialize with 0 sum having one frequency
        cumulative_sum = 0
        count = 0
    
        for num in nums:
            cumulative_sum += num
            if (cumulative_sum - k) in sum_map:
                count += sum_map[cumulative_sum - k]
            sum_map[cumulative_sum] = sum_map.get(cumulative_sum, 0) + 1
    
        return count

    
    nums = [1, 1, 1]
    k = 2
    print(subarray_sum(nums, k))  # Output: 2   
import heapq

class Solution(object):
    def find_Kth_Largest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = []
        for i in nums:
            heapq.heappush(n, (-i, i))
        for j in range(k):
            w, i = heapq.heappop(n)
            if j == k - 1:
                return i

# Test the function
arr_nums = [-1, 14, 9, 50, 61, 41]
S = Solution()

result = S.find_Kth_Largest(arr_nums, 3)
print("Third largest element:", result)

result = S.find_Kth_Largest(arr_nums, 2)
print("Second largest element:", result)

result = S.find_Kth_Largest(arr_nums, 5)
print("Fifth largest element:", result)

result = S.find_Kth_Largest(arr_nums, 4)
print("Fourth largest element:", result)

result = S.find_Kth_Largest(arr_nums, 1)
print("First largest element:", result)

result = S.find_Kth_Largest(arr_nums, 6)
print("Sixth largest element:", result)

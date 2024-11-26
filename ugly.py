import heapq

class Solution(object):
    def nth_ugly_number(self, n):
        Ugly_num = 0
        heap = []
        heapq.heappush(heap, 1)
        seen = {1}
        
        for _ in range(n):
            Ugly_num = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly = Ugly_num * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return Ugly_num

n = 8
S = Solution()
result = S.nth_ugly_number(n)
print(f"{n}th ugly number:", result)

n = 12
result = S.nth_ugly_number(n)
print(f"{n}th ugly number:", result)
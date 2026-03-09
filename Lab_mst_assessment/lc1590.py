class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        ans = n

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]

                if s % p == rem:
                    ans = min(ans, j - i + 1)

        if ans == n:
            return -1
        return ans
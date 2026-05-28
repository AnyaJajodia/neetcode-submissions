class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set()
        max_len = 0
        curr_len = 0
        for num in nums:
            temp.add(num)
            max_len = 1
            curr_len = 1
        for num in nums:
            while num+1 in temp:
                curr_len += 1
                num = num+1
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
        return max_len

                    
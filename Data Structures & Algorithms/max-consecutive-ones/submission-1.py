
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        self.max_len=0
        self.current_streak =0
        nums.append(0)
        
        for i in range(0,len(nums)):
            if nums[i]==1:
                self.current_streak=self.current_streak+1
            else:
                self.max_len= max(self.current_streak, self.max_len)
                self.current_streak=0
        return self.max_len

        # return nums.count(1)
        
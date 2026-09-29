class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        add_pointer =0
        moving_pointer = 0
        for k in range(0,len(nums)):
            if (nums[k]==val ):
                nums[k]=""
            else :
                repl = nums[k]
                nums[k]=""
                nums[add_pointer] = repl
                add_pointer = add_pointer+1
        return add_pointer


        

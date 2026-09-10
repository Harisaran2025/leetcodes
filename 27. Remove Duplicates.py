class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  #temp var for storing next elements
        for i in range(len(nums)):   # for loop with the length of nums var
            if nums[i] != val:    # loop compares i value with val
                nums[k] = nums[i]   # if true it executes
                k += 1  #stores value in k
        return k  
        

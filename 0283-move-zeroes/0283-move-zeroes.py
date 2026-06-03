class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=0
        a=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                a.append(nums[i])
            else:
                c+=1
        for i in range(c):
            a.append(0)
        nums[:]=a
      

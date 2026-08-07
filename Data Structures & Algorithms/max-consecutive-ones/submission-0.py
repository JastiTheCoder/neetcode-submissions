class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_len = ct = 0

        for num in nums:
            if num == 0:
                max_len = max(max_len,ct)
                ct = 0 
            else:
                ct+=1
        
        return max(ct, max_len)
            

           

            
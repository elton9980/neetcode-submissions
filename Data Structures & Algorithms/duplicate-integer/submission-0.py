from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = defaultdict(int)
        
        for num in nums:
            hmap[num] = hmap[num] + 1

        for key,value in hmap.items():
            if value > 1:
                return True
        
        return False 
            
         
        

        
        
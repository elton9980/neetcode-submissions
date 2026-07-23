from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for key,frequency in count.items():
            if frequency > len(nums)/2:
                return key
    
        






        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=defaultdict(int)
        
        
        for num in nums:
            count[num] += 1

        arr = []

        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        res=[]

        while len(res) < k:
            freq,num=arr.pop()
            res.append(num)
        return res
        
        
            
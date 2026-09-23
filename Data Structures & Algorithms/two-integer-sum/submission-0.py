class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            N=nums[i]
            complement=target-N

            if complement in seen:
                return [seen[complement],i]

            seen[N]=i


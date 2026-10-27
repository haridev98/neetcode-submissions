class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif ={}
        for ind ,val in enumerate (nums):
            if val in dif:
                return list ( [ dif[val] , ind ])
            else:
                dif[target - val] = ind



        
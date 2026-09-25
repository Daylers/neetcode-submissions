class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        power = 1
        zero_cnt = 0
        for i in range(len(nums)):
            num = nums[i]
            if nums[i] == 0:
                num = 1
                zero_cnt += 1
            
            power = power * num
        
        for i in range(len(nums)):
            if zero_cnt == 0: 
                lst.append(power // nums[i])
            elif zero_cnt == 1:                
                if nums[i] == 0:
                    lst.append(power)
                else:
                    lst.append(0)
            elif zero_cnt > 1:
                lst.append(0)
        
        return lst
            
        

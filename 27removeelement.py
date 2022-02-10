class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        loc=1
        start = math.floor(len(nums)/2)
        a = len(nums)
        
        if a > 0:
            maxi = nums[a-1]
            mini = nums[0]
            
            if mini > val or maxi < val:
                return a
            elif val == mini:
                while nums[0] == val:
                    del nums[0]
                    if len(nums) < 1:
                        break
                return len(nums)
            elif val == maxi:
                while nums[a-1] == val:
                    del nums[a-1]
                    a = len(nums)
                return len(nums)
            elif nums[start] < val:
                while nums[start] < val:
                    start+=1
                same = True
                while same:
                    if nums[start] == val:
                        del nums[start]
                        a = len(nums)
                    else:
                        same=False
                        break
                return len(nums)
            elif nums[start] > val:
                while nums[start] > val:
                    start-=1
                same = True
                while same:
                    if nums[start] == val:
                        del nums[start]
                        a = len(nums)
                    elif nums[start-1] == val:
                        del nums[start-1]
                        start-=1
                        a = len(nums)
                    else:
                        same = False
                return len(nums)
            elif nums[start] == val:
                same = True
                while same:
                    if nums[start] == val:
                        del nums[start]
                    elif nums[start-1] == val:
                        del nums[start-1]
                        start -=1
                    else:
                        same = False
                return len(nums)
        return a

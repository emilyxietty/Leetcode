class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if x < 0:
            return False
        if x < 10:
            return True
        else:
            count = 0
            iter = math.floor(len(num)/2)
            while count < iter:
                if num[count] == num[len(num)-1-count]:
                    count = count+1
                else:
                    return False
            if count == iter:
                return True

class Solution:
    def isValid(self, s: str) -> bool:
        circle = 0
        square = 0
        curly = 0
        current = []
        for i in range(len(s)):
            if s[i] == "(":
                current.append(1)
                circle+=1
            elif s[i] == "[":
                current.append(2)
                square+=1
            elif s[i] == "{":
                current.append(3)
                curly+=1
            elif circle > 0 and s[i] == ")" and current.pop() == 1:
                circle-=1
            elif square > 0 and s[i] == "]" and current.pop() == 2:
                square-=1
            elif curly > 0 and s[i] == "}" and current.pop() == 3:
                curly-=1
            else:
                return False
        if circle == 0 and square == 0 and curly == 0:
            return True
        else:
            return False

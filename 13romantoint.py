values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i=0
        while i < len(s):
            if i+1 < len(s):
                if s[i] == "I" and (s[i+1] == "X" or s[i+1] == "V"):
                        total = total+values[s[i+1]]-values[s[i]]
                        i=i+1
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                        total = total+values[s[i+1]]-values[s[i]]
                        i=i+1
                elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                        total = total+values[s[i+1]]-values[s[i]]
                        i=i+1
                else:
                    total = total+values[s[i]]
                i = i+1
            else:
                total = total+values[s[i]]
                i = i+1
        return total
            

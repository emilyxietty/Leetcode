class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        firstlet=[]
        i=0
        j=len(haystack)-len(needle)
        while i<=j:
            if haystack[i]==needle[0]:
                firstlet.append(i)
                i+=1
            if haystack[j]==needle[0]:
                firstlet.append(j)
                j-=1
            else:
                i+=1
                j-=1
        if len(firstlet) == 0:
            return -1
        if len(needle) == 1:
            return firstlet[0]
        firstlet.sort()
        test=0
        while test < len(firstlet):
            firstH=firstlet[test]+1
            firstN=1
            lastH=firstlet[test]+len(needle)-1
            lastN=len(needle)-firstN
            while firstN < len(needle):
                if needle[firstN]==haystack[firstH] and needle[lastN]==haystack[lastH]:
                        firstH+=1
                        firstN+=1
                        lastH-=1
                        lastN-=1
                else:
                    break
                if firstN>lastN:
                    return firstlet[test]
            test+=1
        return -1

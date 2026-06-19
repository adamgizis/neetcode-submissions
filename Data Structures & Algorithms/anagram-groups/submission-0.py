from collections import Counter
class Solution:
    def getCounter(self, s: str):
        t = [0 for i in range(26)]
        for c in s:
            t[ord(c)-97]+=1
        
        return tuple(t)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = Counter()
        result = []
        counter = 0
        for s in strs:
            th = self.getCounter(s)
            if th in c:
                result[c[th]].append(s)
            else:
                result.append([s])
                c[th] = counter
                counter+=1
        return result


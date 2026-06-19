from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Counter()
        tmap = Counter()
        for i in s:
            smap[i]+=1
        for i in t:
            tmap[i]+=1

        print(smap, tmap)
        return smap == tmap

        
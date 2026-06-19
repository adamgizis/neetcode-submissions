import queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] +=1

        buckets = {}
        for n in freq.keys():
            if freq[n] not in buckets:
                buckets[freq[n]] = []
            buckets[freq[n]].append(n)

        uniques = sorted(buckets.keys(), reverse=True)
        k_list = []
        i = 0
        while len(k_list) < k:

            k_list = buckets[uniques[i]] + k_list
            i +=1


        return k_list


        
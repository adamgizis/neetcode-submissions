from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        hand.sort()

        count = Counter(hand)

        for i in hand:
            size = groupSize
            if i in count and count[i] > 0 :
                value = i
                while size > 0:
                    if value not in count or count[value] <= 0:
                        print(value)
                        return False
                    count[value]-=1
                    value+=1
                    size-=1
        
        return True

                    
                


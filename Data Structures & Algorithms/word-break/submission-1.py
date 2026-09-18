class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        queue = deque()

        seen_word = set()
        wordDict = set(wordDict)
        queue.append(0)

        while queue:
            index= queue.popleft()
            if index == len(s) :
                return True
            for i in range(index, len(s)):
                if s[index:i+1] in wordDict and (s[index:i+1], index, i) not in seen_word:
                    queue.append(i+1)
                    seen_word.add((s[index:i+1], index, i))



        return False
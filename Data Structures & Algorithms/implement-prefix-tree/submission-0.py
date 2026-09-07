class Node:
    def __init__(self, letter):
        self.letter = letter
        self.end_words = set()
        self.childern = {}

class PrefixTree:

    def __init__(self):
        self.heads ={}
        
    def insert(self, word: str) -> None:
        it = None
        if word[0] not in self.heads:
            it = Node(word[0])
            self.heads[word[0]] = it
        else:
            it = self.heads[word[0]]
        
        count = 1
        while count < len(word):
            if word[count] in it.childern:
                it = it.childern[word[count]]
            else:
                node = Node(word[count])
                it.childern[word[count]] = node
                it = node
            count+=1
        it.end_words.add(word)      
        

    def search(self, word: str) -> bool:
        if word[0] not in self.heads:
            return False
        
        it = self.heads[word[0]]

        count = 1

        count = 1
        while count < len(word):
            if word[count] in it.childern:
                it = it.childern[word[count]]
            else:
                return False
            count+=1

        if word in it.end_words:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.heads:
            return False
        
        it = self.heads[prefix[0]]

        count = 1

        count = 1
        while count < len(prefix):
            if prefix[count] in it.childern:
                it = it.childern[prefix[count]]
            else:
                return False
            count+=1

        return True
        
        
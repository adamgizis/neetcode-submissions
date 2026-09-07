class Node:
    def __init__(self,letter):
        self.end_words = set()
        self.letter = letter
        self.childern = {}
class WordDictionary:

    def __init__(self):
        self.heads = {}

    def addWord(self, word: str) -> None:
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
        it = None
        queue = []
        if word[0] == ".":
            for w in self.heads.values():
                queue.append((w,0))
        elif word[0] not in self.heads:
            return False
        else:
            it = self.heads[word[0]] 
            queue = [(it,0)]
        while queue != []:
            node, index = queue.pop()
            if index == len(word) - 1:
                if node.end_words:
                    return True
                continue
            if word[index+1] == ".":
                for w in node.childern.values():
                    queue.append((w, index+1))
            elif word[index+1] in node.childern:
                queue.append((node.childern[word[index+1]], index+1))
        return False 
            


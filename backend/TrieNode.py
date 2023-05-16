class TrieNode:
    def __init__(self):
        self.children = {}
        self.marked = False
    
    def add(self, word):
        if (len(word) == 0):
            self.marked = True
        else:
            c = word[0]
            if c in self.children:
                x = self.children[c]
            else:
                x = TrieNode()
                self.children[c] = x
            x.add(word[1:])
    
    def contains(self, word):
        if (len(word) == 0):
            return self.marked
        elif word[0] in self.children:
            return self.children[word[0]].contains(word[1:])
        return False
                
    


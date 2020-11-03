# Understanding
# No restriction time/space complexity - 
# consider storing things in separate data structures
# if multiple parts in one word, pick longest part
# if multiples longest parts in one word, pick part that comes first
# return an array that contains strings 
    # modified strings so that parts are surrounded by []
# initialize:
    # results array - contains modified strings
# nested for loop
    # first loop is through words array
        # if word not in d:
            # d[word] = []
        # second loop is through parts
        # if part not in d[word]:

# for elm in results:
    #      

# Planning
#

# Execution
# def findSubstrings(words, parts):

# Refactor/Reflection
# Use a Trie data structure

class Trie(object):
    def __init__(self):
        self.nxt = {}
        self.end = False

    def add(self, word):
        if not word:
            self.end = True
        else:
            self.nxt.setdefault(word[0], Trie()).add(word[1:])

def findSubstrings(words, parts):
    trie = Trie()
    for elm in parts:
        trie.add(elm)
    for idx, w in enumerate(words):
        pos = len(w)
        L = -1
        for j in range(len(w)):
            t = trie
            k = j
            while k < len(w) and w[k] in t.nxt:
                t = t.nxt[w[k]]
                k += 1
                if t.end and k - j > L:
                    L = k - j
                    pos = j
        if L > 0:
            words[idx] = "{}[{}]{}".format(w[:pos], w[pos:pos+L], w[pos+L:])
    return words
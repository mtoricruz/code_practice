# Understanding
# no restriction to space/time complexity
# match each each letter with first letter in words
# once match found check to see if next letter is a neighbor
# continue as matches are made, if none, go to next word
# if duplicate letters are neighbors backtrack
# return an array of words that can be spelled within boggle rules


# Planning
#

# Execute

# Refactor/Reflect
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        # adds word to the trie
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word_end = True
    
    def check_word(self, word):
        # returns a link to the node that has the last character of word
        curr = self.root
        for char in word:
            if char not in curr.children:
                return
            curr = curr.children[char]
        return curr
    
def find_words(board, i, j, trie, used, curr, result):
    # cell doesn't exist or letter has been used already
    if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or used[i][j]:
        return
    
    used[i][j] = True
    curr.append(board[i][j])

    check = trie.check_word(curr)
    if not check: # word doesn't exist in trie
        curr.pop()
        used[i][j] = False
        return
    elif check.word_end:
        result.add(''.join(curr))
    
    for i0 in range(-1, 2):
        for j0 in range(-1, 2):
            if i0 == j0 == 0: # same position as current
                continue
            find_words(board, i+i0, j+j0, trie, used, curr, result)
    curr.pop() # backtracking steps
    used[i][j] = False

def wordBoggle(board, words):
    trie = Trie() # construct a trie out of words
    for word in words:
        trie.add_word(word)
    result = set()
    used = [[False] * len(board[0]) for _ in range(len(board))]
    curr = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            find_words(board, i, j, trie, used, curr, result)
    return sorted(result)    
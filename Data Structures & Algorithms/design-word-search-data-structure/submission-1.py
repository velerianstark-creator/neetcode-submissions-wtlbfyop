class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word.lower():
            if not node.children[ord(ch) - ord('a')]:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            for n in range(len(word)):
                ch = word[n]
                if ch != ".":
                    if not node.children[ord(ch) - ord('a')]:
                        return False
                    node = node.children[ord(ch) - ord('a')]              
                else:
                    for child in node.children:
                        if child:
                            if dfs(child, word[n+1:]):
                                return True
                    return False
            return node.end
        return dfs(self.root, word)

        

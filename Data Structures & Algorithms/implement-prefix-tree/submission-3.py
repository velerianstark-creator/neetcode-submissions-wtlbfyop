class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word.lower():
            if not node.children[ord(ch) - ord('a')]:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word.lower():
            if not node.children[ord(ch) - ord('a')]:
                return False
            node = node.children[ord(ch) - ord('a')]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix.lower():
            if not node.children[ord(ch) - ord('a')]:
                return False
            node = node.children[ord(ch) - ord('a')]
        return True
        
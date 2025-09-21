class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True
        
    def search(self, word: str) -> bool:
        
        node = self.trie

        def search_node(word, node) -> bool:
            for i, ch in enumerate(word):
                # print(word, "-->", ch, "-->", node)
                if ch == ".":
                    for x in node:
                        if x != '$' and search_node(word[i+1:], node[x]):
                            return True
                    return False
                elif ch in node:
                    node = node[ch]
                    continue
                else:
                    return False
            
            if "$" in node:
                return True
            
            return False

        return search_node(word, node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
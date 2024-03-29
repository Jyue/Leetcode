class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True

    def search(self, word: str) -> bool:
        
        def search_in_node(word, node) -> bool:
            for i, char in enumerate(word):
                if char not in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if char == '.':
                        for x in node:
                            if x != '#' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                
                # if the character is found
                else:
                    node = node[char]
            return "#" in node
        
        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
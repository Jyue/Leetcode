class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")


    def insert(self, word: str) -> None:
        node = self.root
        
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            # If a character is not found,
            # create a new node in the trie
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                
        # Mark the end of a word
        node.is_end = True

       

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
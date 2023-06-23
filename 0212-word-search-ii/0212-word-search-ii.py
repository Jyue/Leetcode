class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 建構 Trie
        is_word = '$'
        
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[is_word] = word
        # print(trie)
        
        
        def dfs(r, c, parent):
            
            letter = board[r][c]
            currNode = parent[letter]
            
            # check if we find a match of word
            # 如果is_word存在 => return值並將其pop掉，如果is_word不存在 => return False
            word_match = currNode.pop(is_word, False) 
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                match.append(word_match)
                # print(trie)
            
            # 先標記為visited 
            board[r][c] = '#'
            # 上下左右 dfs
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = r + rowOffset, c + colOffset     
                if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                    continue
                if board[newRow][newCol] not in currNode:
                    continue
                dfs(newRow, newCol, currNode)
            # 結束，回復原狀
            board[r][c] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)
                
        
        
        
        # 遍歷整個table
        m = len(board)
        n = len(board[0])
        match = []
        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        # print(trie)
        return match
        
        
                
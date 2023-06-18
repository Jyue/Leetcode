class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
    	M, N = len(m), len(m[0])
    	for i,j in itertools.product(range(M),range(N)):
    		if m[i][j]: continue
    		for k in range(N):
    			if m[i][k] != 0: m[i][k] = ' '
    		for k in range(M):
    			if m[k][j] != 0: m[k][j] = ' '
    	for i,j in itertools.product(range(M),range(N)):
    		if m[i][j] == ' ': m[i][j] = 0
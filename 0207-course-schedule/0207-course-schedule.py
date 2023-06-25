class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = [[] for _ in range(n)]
        # 計算每個 node 的 indegree。
        indegree = [0] * n
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        # S 是可以參加的所有課程的stack。
        S = [ v for v in range(n) if indegree[v] == 0]
        while S:
            course = S.pop()
            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    S.append(nextCourse)
        return not any(indegree)
            
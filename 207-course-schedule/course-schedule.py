class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for i in range(len(prerequisites)):
            pre[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set()
        def dfs(course):
            if not pre[course]:
                return True
            if course in visited:
                return False
            visited.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            pre[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        cooldown = deque()
        timer = 0

        for k,v in freq.items():
            heapq.heappush(heap, -v)
        
        while heap or cooldown:
            if heap:
                task = -heapq.heappop(heap)
                if task > 1:
                    cooldown.append((task-1, timer+n+1))
            timer += 1

            while cooldown and cooldown[0][1] == timer:
                task_count, _ = cooldown[0]
                cooldown.popleft()
                heapq.heappush(heap, -task_count)
        return timer
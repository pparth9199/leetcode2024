class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        minheap = []
        sans=""
        for k,v in c.items():
            minheap.append((-v,k))

        heapq.heapify(minheap)

        while minheap:
            freq, char = heapq.heappop(minheap)
            sans += char * (-freq)

        return sans
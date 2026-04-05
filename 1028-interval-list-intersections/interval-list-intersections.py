class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1=0
        p2=0
        res = []
        while p1<len(firstList) and p2<len(secondList):
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])
            
            # 2. If start <= end, it's a valid intersection
            if start <= end:
                res.append([start, end])
            
            # 3. Move the pointer for the interval that finishes first
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
                
        return res

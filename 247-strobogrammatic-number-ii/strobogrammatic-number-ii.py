class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'], 
            ['6', '9'], ['8', '8'], ['9', '6']
        ]
        if n==2:
            return ["11","69","88","96"]
        def result(p,up):
            if p==0:
                return [""]
            if p==1:
                return ["0","1","8"]
            prev = result(p-2,up)
            current= []
            for pre in prev:
                for pair in reversible_pairs:
                    if pair[0]!='0' or p!=up:
                        current.append(pair[0]+pre+pair[1])
            return current

        return result(n,n)
      
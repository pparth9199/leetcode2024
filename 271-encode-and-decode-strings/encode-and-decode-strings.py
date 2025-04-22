class Codec:
    def __init__(self):
        self.encoded = ""
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        for i in strs:
            self.encoded+=i + 'å'
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return self.encoded.split('å')[:-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
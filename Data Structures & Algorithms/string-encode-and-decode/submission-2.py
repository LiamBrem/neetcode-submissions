class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string + "ϖ"

        return res
        
    def decode(self, s: str) -> List[str]:
        return s.split("ϖ")[:-1]
        



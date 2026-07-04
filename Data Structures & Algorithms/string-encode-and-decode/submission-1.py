class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = []
        prefix.append(str(len(strs)) + "#")
        for word in strs:
            prefix.append(str(len(word)) + "#")
        return "".join(prefix) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        wordsAmount = 0
        for i in range(len(s)):
            if s[i] == "#":
                wordsAmount = int(s[:i])
                s = s[i+1:]
                break
        lens = [] 
        for i in range(wordsAmount):
            for letter in range(len(s)):
                if s[letter] == "#":
                    lens.append(int(s[:letter])) 
                    s = s[letter+1:]
                    break
        output = []
        for wordLen in lens:
            output.append(s[:wordLen])
            s = s[wordLen:]
        return output





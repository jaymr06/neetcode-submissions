class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToWord = {}
        for word in strs:
            freq = self.wordToFreq(word)
            if freq not in freqToWord:
                freqToWord[freq] = [word]
            else:
                freqToWord[freq].append(word)
        return list(freqToWord.values())

    def wordToFreq(self, word):
        freq = {}
        for letter in word:
            freq[letter] = 1 if letter not in freq else freq[letter] + 1
        return tuple(sorted(freq.items()))
                
            

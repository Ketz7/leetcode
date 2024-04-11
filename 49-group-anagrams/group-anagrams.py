class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comp_dict = {}
        for words in strs:
            sorted_word = ''.join(sorted(words))
            comp_dict[sorted_word] = comp_dict.get(sorted_word, [])
            comp_dict[sorted_word].append(words)
        return comp_dict.values()
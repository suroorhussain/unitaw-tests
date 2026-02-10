# Uses a defaultdict to simplify and slightly speed up the code.
# Note: This was optimised with suggestions from ChatGPT.
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_letters = ''.join(sorted(word))
            groups[sorted_letters].append(word)
        return list(groups.values())
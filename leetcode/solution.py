class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            sorted_letters = ''.join(sorted(word))
            if sorted_letters in groups:
                groups[sorted_letters].append(word)
            else:
                groups[sorted_letters] = [word]
        return list(groups.values())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
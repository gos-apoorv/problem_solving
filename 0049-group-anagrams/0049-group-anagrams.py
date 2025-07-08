class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for t in strs:
            ans[tuple(sorted(t))].append(t)

        return list(ans.values())
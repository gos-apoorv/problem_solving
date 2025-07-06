class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def get_count(word: str) -> list[int]:
            w_list = [0] * 26

            for c in word:
                w_list[ord(c) - ord('a')] += 1
            return w_list

        s_max = [0] * 26
        for sub_str in words2:
            for i, c in enumerate(get_count(sub_str)):
                s_max[i] = max(s_max[i], c)

        univ_list = []
        for word in words1:
            if all(x >=y for x,y in zip(get_count(word), s_max)):
                univ_list.append(word)
        
        return univ_list

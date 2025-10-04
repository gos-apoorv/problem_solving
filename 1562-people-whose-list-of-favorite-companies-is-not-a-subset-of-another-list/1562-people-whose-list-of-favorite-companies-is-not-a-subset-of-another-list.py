class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        ans = []

        for i in range(0, len(favoriteCompanies)):
            subset_flag = False
            for j in range(0, len(favoriteCompanies)):
                if i == j:
                    continue
                else:
                    set_i = set(favoriteCompanies[i])
                    set_j = set(favoriteCompanies[j])

                    if not set_i.issubset(set_j):
                        continue
                    else:
                        subset_flag = True
                        break
            
            if not subset_flag:
                ans.append(i)
        
        return ans


        
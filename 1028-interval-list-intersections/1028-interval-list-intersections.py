class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        def find_intersection(small_list, larger_list):
            temp_list = []
            if len(small_list) < 1 or len(larger_list) < 1:
                return temp_list
            else:
                small_pos = 0
                larger_pos = 0
                while small_pos < len(small_list) and larger_pos < len(larger_list):
                    s_start, s_end = small_list[small_pos]
                    l_start, l_end = larger_list[larger_pos]
                    
                    start = max(s_start, l_start)
                    end = min(s_end, l_end)
                    if start <= end:
                        temp_list.append([start, end])

                    # print(small_list[small_pos], larger_list[larger_pos], '<---->', temp_list )

                    if s_end < l_end:
                        small_pos += 1
                    else:
                        larger_pos += 1

            return temp_list


        intersection = find_intersection(firstList, secondList)

        return intersection
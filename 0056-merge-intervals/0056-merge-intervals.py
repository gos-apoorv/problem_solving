class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        # print(intervals)
        merge_list = []
        new_element = []
        previous_element = intervals[0]
        merge_list.append(previous_element)
        for pos in range(1, len(intervals)):
            if intervals[pos][0] <= previous_element[1] and intervals[pos][1] > previous_element[1]:
                new_element = [previous_element[0], intervals[pos][1]]
                merge_list.pop()
            elif intervals[pos][0] <= previous_element[1] and intervals[pos][1] <= previous_element[1]:
                continue
            else:
                new_element = [intervals[pos][0], intervals[pos][1]]
            merge_list.append(new_element)
            previous_element = new_element
            # print(merge_list)

        # print(merge_list)
        return merge_list            


        
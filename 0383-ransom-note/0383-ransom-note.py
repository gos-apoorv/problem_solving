from typing import Dict
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Create hashmap of a string with its frequency
        def createHashMap(input_string: str) -> Dict[str, int]:
            letter_map = {}
            for t in input_string:
                if letter_map.get(t):
                    letter_map[t] = letter_map[t] + 1
                else:
                    letter_map[t] = 1
            return letter_map

        magazineMap = createHashMap(magazine)

        for t in ransomNote:
            if magazineMap.get(t) is not None and magazineMap.get(t) > 0 :
                magazineMap[t] = magazineMap[t] - 1
            else:
                return False
        
        return True
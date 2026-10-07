from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combinations = []
        n = len(strs)
        visited = [False] * n
        
        for i in range(n):
            if visited[i]:
                continue

            word = strs[i]
            visited[i] = True
            current_group = [word]

            for j in range(i + 1, n):
                candidate = strs[j]
                if not visited[j] and len(word) == len(candidate):
                    temp_word = word
                    is_anagram = True
                    for letter in candidate:
                        if letter in temp_word:
                            temp_word = temp_word.replace(letter, "", 1)
                        else:
                            is_anagram = False
                            break
                    if is_anagram and len(temp_word) == 0:
                        visited[j] = True
                        current_group.append(candidate)
                        
            combinations.append(current_group)
            
        return combinations
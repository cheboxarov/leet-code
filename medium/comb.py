from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                combinations.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        combinations = []
        backtrack(0, target, [])
        return combinations

# Пример использования
print(Solution().combinationSum([2, 3, 6, 7], 7))

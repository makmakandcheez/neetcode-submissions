class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        p1 = numbers[i]
        p2 = numbers[j]

        while i < len(numbers)-1 and j > 0:
            if p1 + p2 < target:
                i += 1
                p1 = numbers[i]
            elif p1 + p2 > target:
                j -= 1
                p2 = numbers[j]
            else:
                return [i+1, j+1]
        
        return None


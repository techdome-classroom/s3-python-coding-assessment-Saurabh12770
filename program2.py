"""
class Solution(object):
    def romanToInt(s: str) -> int:
        roman_map={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total=0
        prev_value=0
        for char in reversed(s):
            current_value=roman_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total
"""
# example
# print(romanToInt("III"))


class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Iterate through each character in the string
        for i in range(n):
            # If the current numeral is smaller than the next one, subtract its value
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add its value
                total += roman_map[s[i]]
        
        return total

# Testing the solution with examples
#solution = Solution()
#print(solution.romanToInt("III"))       # Output: 3
#print(solution.romanToInt("LVIII"))     # Output: 58
#print(solution.romanToInt("MCMXCIV"))   # Output: 1994


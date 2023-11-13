class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_indices = [i for i, char in enumerate(s) if char in vowels]

        sorted_vowels = sorted([char for char in s if char in vowels])

        result = list(s)
        for i, vowel_index in enumerate(vowel_indices):
            result[vowel_index] = sorted_vowels[i]

        return ''.join(result)

# Example usage:
solution = Solution()
result1 = solution.sortVowels("lEetcOde")
result2 = solution.sortVowels("lYmpH")

print(result1)  # Output: "lEOtcede"
print(result2)  # Output: "lYmpH"

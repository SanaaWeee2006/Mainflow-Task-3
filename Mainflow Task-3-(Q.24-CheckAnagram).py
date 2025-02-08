# ---8. Check if two strings are anagrams (contain the same characters in any order).

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

print("Anagram:", is_anagram(s1, s2))


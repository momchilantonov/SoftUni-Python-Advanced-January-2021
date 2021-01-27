def palindrome(word, idx=0):
    if idx >= len(word) // 2:
        return f"{word} is a palindrome"
    if word[idx] == word[-idx-1]:
        return palindrome(word, idx+1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abccba", 0))
print(palindrome("peter", 0))

# def palindrome(line, ind):
#     a = palindrome1(line, 0)
#     if a:
#         return f'{line} is a palindrome'
#     else:
#         return f'{line} is not a palindrome'
#
#
# def palindrome1(line1, ind):
#     if len(line1) == 1:
#         return True
#     if line1[0] != line1[-1]:
#         return False
#     return palindrome1(line1[1:-1], ind)
#
#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))

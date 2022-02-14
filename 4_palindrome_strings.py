palindrome_strings = input().split()
palindrome_word = input()

print([w for w in palindrome_strings if w[::-1] == w])
print(f"Found palindrome {palindrome_strings.count(palindrome_word)} times")

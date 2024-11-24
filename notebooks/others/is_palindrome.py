print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))
print("-" * 30)

def is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Racecar"))
print(is_palindrome("Race car"))
print(is_palindrome(""))
print(is_palindrome("a"))
print(is_palindrome("ab"))
print(is_palindrome("aba"))
print(is_palindrome("abba"))
print("-" * 30)

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Testando a função com alguns exemplos
print(is_palindrome("radar"))  # True
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check the substring without the first and last characters
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def is_palindrome_tail(s):
    def helper(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return helper(left + 1, right - 1)
    return helper(0, len(s) - 1)
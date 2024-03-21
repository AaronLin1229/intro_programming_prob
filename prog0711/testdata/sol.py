def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != '(':
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

s = input()
print(is_valid_parentheses(s))

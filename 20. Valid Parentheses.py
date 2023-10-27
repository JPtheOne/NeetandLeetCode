# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Time O(n), Space O(n)
def isValid(s):
    s = "(]"
    stack = []
    yup = True

    for i in s:
        if i=="(":
            stack.append(")")
        elif i=="[":
            stack.append("]")
        elif i=="{":
            stack.append("}")
        else:
            if not stack:
                yup = False
            elif stack[-1]==i:
                stack.pop()
            else:
                yup = False


    if not stack and yup:
        return True
    else:
        return False

# 3 steps
# if opening, append closing to stack
# if closing, see if last added in stack matches and pop
# if it does not match and stack is empty, end. Otherwise ,True
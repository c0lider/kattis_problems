input()
brackets = input()
stack = []
opening_brackets = "([{"
closing_brackets = ")]}"
corresponding_brackets = {"(": ")", "[": "]", "{": "}"}

for bracket in brackets:
    if bracket in opening_brackets:
        stack.append(bracket)
    elif bracket in closing_brackets:
        if not stack or corresponding_brackets[stack[-1]] != bracket:
            print("Invalid")
            exit()
        stack.pop()
    else:
        print("Invalid")
        exit()


if not stack:
    print("Valid")
else:
    print("Invalid")

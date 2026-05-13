inp = input("Enter string : ")

stack = []

for ch in inp:
    stack.append(ch)

    while ''.join(stack[-2:]) == 'ab':
        stack.pop()
        stack.pop()
        stack.append('S')

    while len(stack)>=3 and ''.join(stack[-3:]) == 'aSb':
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append('S')

if stack == ['S']:
    print("Accepted")
else:
    print("Rejected")
    
# grammar
# S -> aSb | ab

# accepted string
# aaabbb
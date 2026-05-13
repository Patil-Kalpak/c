stack = ['$','S']
inp = input("Enter string : ") + '$'

table = {
    ('S','a') : 'aSb',
    ('S','b') : '',
    ('S','$') : ''
}

i = 0

while stack:
    top = stack.pop()

    if top == inp[i]:
        i += 1

    elif top.isupper():

        if (top,inp[i]) in table:
            prod = table[(top,inp[i])]

            for ch in reversed(prod):
                stack.append(ch)
        else:
            print("Rejected")
            exit()

    else:
        print("Rejected")
        exit()

if inp[i] == '$':
    print("Accepted")
else:
    print("Rejected")
    
# grammar
# S -> aSb | e

# accepted string
# aabb
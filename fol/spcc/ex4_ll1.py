stack = ['$','E']
inp = input("Enter string : ") + '$'

table = {
    ('E','a') : 'aA',
    ('A','b') : 'b'
}

i = 0

while stack:
    top = stack.pop()

    if top == inp[i]:
        i += 1

    elif (top,inp[i]) in table:
        rule = table[(top,inp[i])]

        for ch in reversed(rule):
            stack.append(ch)

    else:
        print("Rejected")
        exit()

if inp[i] == '$':
    print("Accepted")
else:
    print("Rejected")
    
# grammar

# E -> aA
# A -> b
# accepted string
# ab
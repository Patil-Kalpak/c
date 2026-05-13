# Left Recursion Removal + FIRST + FOLLOW

grammar = {}
first = {}
follow = {}

n = int(input("Enter number of productions : "))

for _ in range(n):
    s = input()
    lhs, rhs = s.split("->")
    grammar[lhs] = rhs.split("|")

# Remove Left Recursion
newg = {}

for A in grammar:
    alpha = []
    beta = []

    for rule in grammar[A]:
        if rule[0] == A:
            alpha.append(rule[1:])
        else:
            beta.append(rule)

    if alpha:
        A1 = A + "'"
        newg[A] = [b + A1 for b in beta]
        newg[A1] = [a + A1 for a in alpha] + ['e']
    else:
        newg[A] = grammar[A]

print("\nAfter Removing Left Recursion:\n")

for k,v in newg.items():
    print(k,"->"," | ".join(v))

# FIRST
def findFirst(X):
    if X not in newg:
        return {X}

    res = set()

    for prod in newg[X]:
        if prod[0].islower():
            res.add(prod[0])
        else:
            res |= findFirst(prod[0])

    return res

# FOLLOW
def findFollow(X):
    res = set()

    if X == start:
        res.add('$')

    for A in newg:
        for prod in newg[A]:
            for i in range(len(prod)):
                if prod[i] == X:
                    if i+1 < len(prod):
                        nxt = prod[i+1]

                        if nxt.islower():
                            res.add(nxt)
                        else:
                            res |= findFirst(nxt)

                    elif A != X:
                        res |= findFollow(A)

    return res

start = list(newg.keys())[0]

print("\nNT\tFIRST\tFOLLOW")
print("--------------------------------")

for nt in newg:
    first[nt] = findFirst(nt)
    follow[nt] = findFollow(nt)

    print(nt,"\t",first[nt],"\t",follow[nt])
    
    
# sample i/p
# Enter number of productions :
# 2
# E->E+T|T
# T->T*F|F

# sample o/p
# After Removing Left Recursion:

# E -> TE'
# E' -> +TE' | e
# T -> FT'
# T' -> *FT' | e

# NT      FIRST       FOLLOW
# --------------------------------
# E       {'F'}       {'$'}
# E'      {'+'}       {'$'}
# T       {'F'}       {'$'}
# T'      {'*'}       {'$'}

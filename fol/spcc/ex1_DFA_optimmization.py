# RE to DFA (nullable, firstpos, lastpos, followpos)

pos = 1
follow = {}

class Node:
    def __init__(self, val, left=None, right=None):
        global pos
        self.val = val
        self.left = left
        self.right = right
        self.nullable = False
        self.firstpos = set()
        self.lastpos = set()

        if val.isalpha():
            self.pos = pos
            follow[pos] = set()
            pos += 1
        else:
            self.pos = None

def compute(n):
    if n.val.isalpha():
        n.nullable = False
        n.firstpos = {n.pos}
        n.lastpos = {n.pos}

    elif n.val == '|':
        compute(n.left)
        compute(n.right)
        n.nullable = n.left.nullable or n.right.nullable
        n.firstpos = n.left.firstpos | n.right.firstpos
        n.lastpos = n.left.lastpos | n.right.lastpos

    elif n.val == '.':
        compute(n.left)
        compute(n.right)

        n.nullable = n.left.nullable and n.right.nullable

        if n.left.nullable:
            n.firstpos = n.left.firstpos | n.right.firstpos
        else:
            n.firstpos = n.left.firstpos

        if n.right.nullable:
            n.lastpos = n.left.lastpos | n.right.lastpos
        else:
            n.lastpos = n.right.lastpos

        for i in n.left.lastpos:
            follow[i] |= n.right.firstpos

    elif n.val == '*':
        compute(n.left)
        n.nullable = True
        n.firstpos = n.left.firstpos
        n.lastpos = n.left.lastpos

        for i in n.lastpos:
            follow[i] |= n.firstpos

# Example RE : (a|b)*.a
a = Node('a')
b = Node('b')
or1 = Node('|', a, b)
star = Node('*', or1)
a2 = Node('a')
root = Node('.', star, a2)

compute(root)

# Print details
nodes = [a, b, or1, star, a2, root]

for n in nodes:
    print("\nNode :", n.val)
    print("Nullable :", n.nullable)
    print("Firstpos :", n.firstpos)
    print("Lastpos :", n.lastpos)

print("\nFollowpos")
for k,v in follow.items():
    print(k, ":", v)

# Simple DFA table
print("\nState Transition Table")
print("State\t a \t b")
print("A\t B \t A")
print("B\t B \t A")
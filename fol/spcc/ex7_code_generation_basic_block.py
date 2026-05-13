n = int(input("Enter number of statements: "))

code = []

print("Enter Three Address Code:")

for i in range(n):
    code.append(input())

leaders = [0]

# Find Leaders
for i in range(n):

    if "goto" in code[i]:

        parts = code[i].split()

        target = int(parts[-1]) - 1

        if target not in leaders:
            leaders.append(target)

        if i + 1 < n and (i + 1) not in leaders:
            leaders.append(i + 1)

leaders.sort()

# Create Basic Blocks
blocks = []

for i in range(len(leaders)):

    start = leaders[i]

    if i + 1 < len(leaders):
        end = leaders[i + 1]
    else:
        end = n

    blocks.append(code[start:end])

# Print Basic Blocks
print("\nBasic Blocks:\n")

for i,b in enumerate(blocks):

    print("B",i+1)

    for stmt in b:
        print(stmt)

    print()

# Flow Graph
print("Flow Graph:\n")

for i,b in enumerate(blocks):

    last = b[-1]

    if "goto" in last:

        target = int(last.split()[-1]) - 1

        for j,l in enumerate(leaders):

            if l == target:
                print(f"B{i+1} --> B{j+1}")

        if "if" in last and i+1 < len(blocks):
            print(f"B{i+1} --> B{i+2}")

    elif i+1 < len(blocks):
        print(f"B{i+1} --> B{i+2}")
        
        
# sample i/p
# Enter number of statements:
# 6

# a=b+c
# if a<10 goto 5
# d=a+b
# goto 6
# x=y+z
# end

# sample o/p
# Basic Blocks:

# B1
# a=b+c
# if a<10 goto 5

# B2
# d=a+b
# goto 6

# B3
# x=y+z

# B4
# end

# Flow Graph:

# B1 --> B3
# B1 --> B2
# B2 --> B4
# B3 --> B4
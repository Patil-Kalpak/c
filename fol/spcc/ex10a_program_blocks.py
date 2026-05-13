blocks = {}
loc = {}

start = int(input("Enter Start Address: "),16)

n = int(input("Enter number of lines: "))

current = "DEFAULT"

blocks[current] = 0

print("Enter Program:")

for _ in range(n):

    line = input().split()

    if not line:
        continue

    # USE Directive
    if line[0] == "USE":

        current = line[1]

        if current not in blocks:
            blocks[current] = 0

    # Instructions
    elif line[0] in ["LDA","STA","ADD","SUB","MUL","DIV","JMP"]:
        blocks[current] += 3

    # RESW
    elif len(line) >= 3 and line[1] == "RESW":
        blocks[current] += int(line[2]) * 3

# Assign Addresses
addr = start

print("\nBlock Table\n")

print("Block No\tBlock Name\tStart Addr\tLength")

for i,(b,l) in enumerate(blocks.items()):

    print(i,"\t\t",b,"\t\t",hex(addr)[2:].upper(),
          "\t\t",hex(l)[2:].upper())

    addr += l
    
    
# sample i/p------
# Enter Start Address: 1000
# Enter number of lines: 14

# USE CODE
# LDA ALPHA
# STA BETA
# USE DATA
# ALPHA RESW 2
# BETA RESW 3
# USE EXTRA
# TEMP RESW 1
# USE CODE
# ADD ALPHA
# SUB TEMP
# USE DATA
# GAMMA RESW 1
# USE EXTRA
# DELTA RESW 2

# sample o/p---------
# Block Table

# Block No   Block Name   Start Addr   Length

# 0          DEFAULT      1000         0
# 1          CODE         1000         C
# 2          DATA         100C         12
# 3          EXTRA        101E         9

optab = {
    "LDA":"00",
    "STA":"20",
    "JMP":"10"
}

loc = 0
symtab = {}
obj = []

n = int(input("Enter number of lines: "))

code = []

for _ in range(n):
    code.append(input().split())

prog = code[0][0]
start = int(code[0][2])

loc = start

# PASS 1 -> Symbol Table
for line in code[1:]:

    if line[0] != '-':
        label = line[0]

        if line[1] != "EQU":
            symtab[label] = loc

        else:
            symtab[label] = line[2]

    op = line[1]

    if op in optab:
        loc += 3

    elif op == "BYTE":
        val = line[2][2:-1]
        loc += len(val)

length = loc - start

# PASS 2 -> Object Code
for line in code[1:]:

    op = line[1]

    if op in optab:
        opcode = optab[op]
        addr = line[2].replace('#','')
        obj.append(opcode + addr)

    elif op == "BYTE":
        s = line[2][2:-1]

        hx = ""

        for ch in s:
            hx += hex(ord(ch))[2:].upper()

        obj.append(hx)

# H Record
print("\nH Record")
print(f"H^{prog}^{start:06X}^{length:06X}")

# T Record
text = ''.join(obj)

print("\nT Record")
print(f"T^{start:06X}^{length:02X}^{text}")

# M Record (dummy example)
print("\nM Record")
print(f"M^{start+1:06X}^05")

# E Record
print("\nE Record")
print(f"E^{start:06X}")

# Symbol Table
print("\nSymbol Table")

print("Symbol\tValue")

for k,v in symtab.items():

    if isinstance(v,int):
        print(k,"\t",hex(v)[2:].upper())
    else:
        print(k,"\t",v)
        
        
# sample ip
# 7
# PG2 START 1000
# - JMP ADD1
# - JMP ADD2
# ADD1 LDA #1020
# - STA #3040
# ADD2 LDA #1004
# DATA1 BYTE C'ABC'


# sample op
# H^PG2^0003E8^000012

# T^0003E8^12^10100610100C001020203040001004414243

# M^0003E9^05

# E^0003E8

# Symbol Table

# ADD1   3EE
# ADD2   3F4
# DATA1  3F7
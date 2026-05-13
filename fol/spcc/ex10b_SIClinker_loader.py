estab = {}

progaddr = int(input("Enter PROGADDR (Hex): "),16)

n = int(input("Enter number of object program lines: "))

lines = []

for _ in range(n):
    lines.append(input())

csaddr = progaddr

memory = {}

# PASS 1 -> ESTAB
for line in lines:

    parts = line.split('^')

    if parts[0] == 'H':

        prog = parts[1]
        length = int(parts[3],16)

        estab[prog] = csaddr

        current = prog

    elif parts[0] == 'D':

        for i in range(1,len(parts),2):

            sym = parts[i]
            addr = int(parts[i+1],16)

            estab[sym] = csaddr + addr

        csaddr += length

# Display ESTAB
print("\nESTAB TABLE\n")

print("Control Section\tSymbol\tAddress")

for k,v in estab.items():
    print(k,"\t\t-\t",hex(v)[2:].upper())

# PASS 2 -> Loading
csaddr = progaddr

for line in lines:

    parts = line.split('^')

    # Header
    if parts[0] == 'H':

        current = parts[1]
        csaddr = estab[current]

    # Text Record
    elif parts[0] == 'T':

        start = int(parts[1],16)

        obj = parts[3]

        addr = csaddr + start

        for i in range(0,len(obj),6):

            memory[addr] = obj[i:i+6]
            addr += 3

    # Modification Record
    elif parts[0] == 'M':

        modaddr = csaddr + int(parts[1],16)

        symbol = parts[3][1:]

        if modaddr in memory:

            old = int(memory[modaddr],16)

            new = old + estab[symbol]

            memory[modaddr] = hex(new)[2:].upper()

# Final Memory Map
print("\nFinal Memory Map\n")

for k,v in sorted(memory.items()):
    print(hex(k)[2:].upper(),":",v)
    
# sample ip
# Enter PROGADDR (Hex): 4000

# Enter number of object program lines:
# 9

# H^PROG1^000000^00107A
# D^ALPHA^000030
# T^000000^1E^1410332810303010154810393C1003
# M^000006^05^+PROG2
# E^000000

# H^PROG2^000000^00003A
# D^BETA^000015
# T^000000^1E^1410332810303010154810393C1003
# E^000000




# sample op
# ESTAB TABLE

# Control Section   Symbol   Address

# PROG1             -        4000
# ALPHA             -        4030
# PROG2             -        507A
# BETA              -        508F

# Final Memory Map

# 4000 : 141033
# 4003 : 281030
# 4006 : 30508F
# 4009 : 481039
# 507A : 141033
# 507D : 281030

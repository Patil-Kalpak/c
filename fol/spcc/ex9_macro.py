mnt = []
mdt = []
ala = {}

inside = False
macro_name = ""

f = open("input.asm","r")
lines = f.readlines()

print("\nExpanded Code:\n")

for line in lines:

    words = line.strip().split()

    if not words:
        continue

    # MACRO START
    if words[0] == "MACRO":
        inside = True
        continue

    # Macro Definition
    if inside:

        if macro_name == "":

            macro_name = words[0]

            params = words[1:]

            mnt.append(macro_name)

            ala[macro_name] = params

            mdt.append(line.strip())

        elif words[0] == "MEND":

            mdt.append("MEND")

            inside = False
            macro_name = ""

        else:
            mdt.append(line.strip())

    # Macro Call
    elif words[0] in mnt:

        actual = words[1:]

        formal = ala[words[0]]

        print("; Expanded Code")

        for stmt in mdt:

            if stmt == "MEND":
                break

            temp = stmt

            for i in range(len(formal)):
                temp = temp.replace(formal[i],actual[i])

            print(temp)

    else:
        print(line.strip())

# DISPLAY TABLES
print("\nMNT")
for i,m in enumerate(mnt):
    print(i+1,m)

print("\nMDT")
for i,m in enumerate(mdt):
    print(i+1,m)

print("\nALA")

for k,v in ala.items():
    print(k,"->",v)
    
    
# sample op :-
# Expanded Code:

# ; Expanded Code
# INCR A,B
# LDA A
# ADD B
# STA A

# START
# END

# MNT
# 1 INCR

# MDT
# 1 INCR &ARG1,&ARG2
# 2 LDA &ARG1
# 3 ADD &ARG2
# 4 STA &ARG1
# 5 MEND

# ALA
# INCR -> ['&ARG1,&ARG2']
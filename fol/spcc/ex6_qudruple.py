stack = []
temp = 1

exp = input("Enter Postfix Expression:\n").split()

print("\nQuadruple Representation\n")

print("+----------+------+-------+--------+")
print("| Operator | Arg1 | Arg2  | Result |")
print("+----------+------+-------+--------+")

for ch in exp:

    if ch.isalnum():
        stack.append(ch)

    else:
        op2 = stack.pop()
        op1 = stack.pop()

        t = "t" + str(temp)

        print(f"|    {ch}     |  {op1}   |   {op2}   |   {t}   |")

        stack.append(t)
        temp += 1

print("+----------+------+-------+--------+")
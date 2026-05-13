# Morphological Analysis

prefixes = ["un", "re", "inter"]
suffixes = ["ness", "ed", "al"]

words = ["unhappiness", "replayed", "international"]

for word in words:

    print("\nWord:", word)

    root = word
    prefix = ""
    suffix = ""

    # Check prefix
    for p in prefixes:
        if word.startswith(p):
            prefix = p
            root = word[len(p):]

    # Check suffix
    for s in suffixes:
        if root.endswith(s):
            suffix = s
            root = root[:-len(s)]

    # Convert happi -> happy
    if root.endswith("i"):
        root = root[:-1] + "y"

    # Print result
    if prefix:
        print(prefix, "-> Bound Morpheme (Prefix)")

    print(root, "-> Free Morpheme (Root Word)")

    if suffix:
        print(suffix, "-> Bound Morpheme (Suffix)")
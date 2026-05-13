# BLEU Score (Simple Version)

# Input sentences
reference = input("Enter reference sentence: ").lower().split()
candidate = input("Enter candidate sentence: ").lower().split()

# Count matching words
match = 0

for word in candidate:
    if word in reference:
        match += 1

# Calculate BLEU score
bleu_score = match / len(candidate)

print("\nMatching Words =", match)
print("Total Candidate Words =", len(candidate))
print("BLEU Score =", round(bleu_score, 2))
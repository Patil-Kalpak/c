# Naive Bayes Classification

sports_prob = {
    "match": 0.5,
    "team": 0.4,
    "win": 0.6,
    "player": 0.7
}

politics_prob = {
    "election": 0.8,
    "vote": 0.7,
    "minister": 0.6,
    "win": 0.3
}

sentence = input("Enter test sentence: ").lower().split()

sports_score = 1
politics_score = 1

for word in sentence:

    if word in sports_prob:
        sports_score *= sports_prob[word]

    if word in politics_prob:
        politics_score *= politics_prob[word]

print("Sports Probability =", sports_score)
print("Politics Probability =", politics_score)

if sports_score > politics_score:
    print("Sentence belongs to SPORTS class")

elif politics_score > sports_score:
    print("Sentence belongs to POLITICS class")

else:
    print("Cannot classify")
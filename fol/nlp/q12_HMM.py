# Hidden Markov Model (HMM) Basics

# Transition Probabilities
transition = {
    "Rainy": {"Rainy": 0.7, "Sunny": 0.3},
    "Sunny": {"Rainy": 0.4, "Sunny": 0.6}
}

# Emission Probabilities
emission = {
    "Rainy": {"Walk": 0.1, "Shop": 0.4, "Clean": 0.5},
    "Sunny": {"Walk": 0.6, "Shop": 0.3, "Clean": 0.1}
}

# Display Transition Probabilities
print("Transition Probabilities:\n")

for state in transition:
    for next_state in transition[state]:
        print(state, "->", next_state, "=", transition[state][next_state])

# Display Emission Probabilities
print("\nEmission Probabilities:\n")

for state in emission:
    for activity in emission[state]:
        print(state, "->", activity, "=", emission[state][activity])
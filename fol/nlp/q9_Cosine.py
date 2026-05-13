# Cosine Similarity (Manual Calculation)

import math

# Input vectors
v1 = [1, 2, 3]
v2 = [2, 4, 6]

# Dot product
dot_product = 0

for i in range(len(v1)):
    dot_product += v1[i] * v2[i]

# Magnitude of vectors
mag1 = 0
mag2 = 0

for i in v1:
    mag1 += i * i

for i in v2:
    mag2 += i * i

mag1 = math.sqrt(mag1)
mag2 = math.sqrt(mag2)

# Cosine similarity
cosine_similarity = dot_product / (mag1 * mag2)

# Display output
print("Vector 1 =", v1)
print("Vector 2 =", v2)

print("\nDot Product =", round(dot_product, 2))
print("Magnitude of Vector 1 =", round(mag1, 2))
print("Magnitude of Vector 2 =", round(mag2, 2))
print("Cosine Similarity =", round(cosine_similarity, 2))
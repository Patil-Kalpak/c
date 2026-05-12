# EXP 6 : Object Detection using Pretrained HOG + SVM Model

# Install once before running:
# pip install opencv-python matplotlib

# ---------------------------------------------------
# Import Libraries
# ---------------------------------------------------

import cv2
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------
# Load Pretrained HOG + SVM Detector
# ---------------------------------------------------

# HOG + SVM pretrained human detector
hog = cv2.HOGDescriptor()

hog.setSVMDetector(
    cv2.HOGDescriptor_getDefaultPeopleDetector()
)

# ---------------------------------------------------
# LOAD IMAGE
# ---------------------------------------------------

# ---------------- SYNTHETIC / CUSTOM IMAGE ----------------

# Use your own custom image
image_path = "sample.jpg"

# ---------------- DATASET (ZIP EXTRACTED FOLDER) ----------------

# First extract the zip folder manually

# Example:
# datasets/
# ├── traffic/
# ├── animals/
# └── custom/

# Uncomment below to use dataset image

# dataset_folder = "datasets/custom"

# Get first image from dataset folder
# image_name = os.listdir(dataset_folder)[0]

# Full image path
# image_path = os.path.join(dataset_folder, image_name)

# ---------------------------------------------------
# Read Image
# ---------------------------------------------------

image = cv2.imread(image_path)

# Check image
if image is None:

    print("Image not found")
    exit()

# Convert BGR to RGB
image_rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

# ---------------------------------------------------
# Perform Object Detection
# ---------------------------------------------------

boxes, weights = hog.detectMultiScale(
    image_rgb,
    winStride=(8, 8),
    padding=(8, 8),
    scale=1.05
)

# ---------------------------------------------------
# Draw Bounding Boxes
# ---------------------------------------------------

for i, (x, y, w, h) in enumerate(boxes):

    # Draw rectangle
    cv2.rectangle(
        image_rgb,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    # Confidence score
    confidence = float(weights[i])

    # Print detection details
    print(
        "Object",
        i + 1,
        "| Confidence Score :",
        round(confidence, 2)
    )

    # Put confidence text
    cv2.putText(
        image_rgb,
        f"{round(confidence,2)}",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

# ---------------------------------------------------
# Display Output Image
# ---------------------------------------------------

plt.figure(figsize=(10, 8))

plt.imshow(image_rgb)

plt.title("Object Detection using HOG + SVM")

plt.axis("off")

plt.show()

# ---------------------------------------------------
# Low Quality Image Test
# ---------------------------------------------------

# Blur image to reduce quality
blurred_image = cv2.GaussianBlur(
    image_rgb,
    (45, 45),
    0
)

# Detect objects again
boxes_blur, weights_blur = hog.detectMultiScale(
    blurred_image,
    winStride=(8, 8)
)

print(
    "\nObjects Detected in Blurred Image :",
    len(boxes_blur)
)

# ---------------------------------------------------
# Display Blurred Image
# ---------------------------------------------------

plt.figure(figsize=(10, 8))

plt.imshow(blurred_image)

plt.title("Low Quality Blurred Image")

plt.axis("off")

plt.show()

# ---------------------------------------------------
# Analysis
# ---------------------------------------------------

print("\nAnalysis:")

print("1. Pretrained HOG + SVM model detected humans in the image.")

print("2. Confidence score indicates detection accuracy.")

print("3. Multiple objects can be detected in one image.")

print("4. Detection may fail because of:")
print("   - Blurry images")
print("   - Low lighting")
print("   - Small objects")
print("   - Occlusion")

print("5. High quality images improve detection performance.")

print("6. Pretrained models reduce training time.")
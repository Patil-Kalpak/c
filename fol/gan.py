# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Dense,Flatten,Reshape,Input
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import mnist
# Heading
print("=========================================")
print("   EXP 10: GAN (GENERATIVE MODELS)       ")
print("=========================================")
# Load MNIST Dataset
(X_train,_),(_,_)=mnist.load_data()
# Normalize Images Between -1 and 1
X_train=(X_train.astype(np.float32)-127.5)/127.5
# Flatten Images
X_train=X_train.reshape(-1,784)
# Print Dataset Shape
print("Training Data Shape :",X_train.shape)
# Generator Model
def build_generator():
    model=Sequential([
        # Input Noise
        Input(shape=(100,)),
        # Hidden Layer
        Dense(256,activation='relu'),
        # Hidden Layer
        Dense(512,activation='relu'),
        # Output Fake Image
        Dense(784,activation='tanh')
    ])
    return model
# Discriminator Model
def build_discriminator():
    model=Sequential([
        # Input Image
        Input(shape=(784,)),
        # Hidden Layer
        Dense(512,activation='relu'),
        # Hidden Layer
        Dense(256,activation='relu'),
        # Output Real or Fake
        Dense(1,activation='sigmoid')
    ])
    # Compile Discriminator
    model.compile(
        loss='binary_crossentropy',
        optimizer=Adam(0.0002,0.5),
        metrics=['accuracy']
    )
    return model
# Create Generator
generator=build_generator()
# Create Discriminator
discriminator=build_discriminator()
# Freeze Discriminator
discriminator.trainable=False
# GAN Input
gan_input=Input(shape=(100,))
# Generate Fake Image
fake_img=generator(gan_input)
# GAN Output
gan_output=discriminator(fake_img)
# Build GAN
gan=Model(gan_input,gan_output)
# Compile GAN
gan.compile(
    loss='binary_crossentropy',
    optimizer=Adam(0.0002,0.5)
)
# Training Parameters
epochs=1000
batch_size=64
sample_interval=200
# Store Losses
d_losses=[]
g_losses=[]
# Start Training
print("\nStarting GAN Training...")
# Training Loop
for epoch in range(epochs+1):
    # Select Real Images
    idx=np.random.randint(0,X_train.shape[0],batch_size)
    real_imgs=X_train[idx]
    # Generate Random Noise
    noise=np.random.normal(0,1,(batch_size,100))
    # Generate Fake Images
    fake_imgs=generator.predict(noise,verbose=0)
    # Train Discriminator on Real Images
    d_loss_real=discriminator.train_on_batch(
        real_imgs,
        np.ones((batch_size,1))
    )
    # Train Discriminator on Fake Images
    d_loss_fake=discriminator.train_on_batch(
        fake_imgs,
        np.zeros((batch_size,1))
    )
    # Average Discriminator Loss
    d_loss=0.5*np.add(
        d_loss_real[0],
        d_loss_fake[0]
    )
    # Train Generator
    noise=np.random.normal(0,1,(batch_size,100))
    g_loss=gan.train_on_batch(
        noise,
        np.ones((batch_size,1))
    )
    # Print Loss Every 100 Epochs
    if epoch%100==0:
        print(f"Epoch {epoch} | D Loss: {d_loss:.4f} | G Loss: {float(g_loss):.4f}")
        d_losses.append(d_loss)
        g_losses.append(float(g_loss))
    # Save Generated Images
    if epoch%sample_interval==0:
        r,c=2,5
        noise=np.random.normal(0,1,(r*c,100))
        gen_imgs=generator.predict(noise,verbose=0)
        # Rescale Images
        gen_imgs=0.5*gen_imgs+0.5
        fig,axs=plt.subplots(r,c)
        cnt=0
        for i in range(r):
            for j in range(c):
                axs[i,j].imshow(
                    gen_imgs[cnt].reshape(28,28),
                    cmap='gray'
                )
                axs[i,j].axis('off')
                cnt+=1
        # Save Images
        plt.savefig(f"Exp10_Iteration_{epoch}.png")
        plt.close()
# Plot Loss Graph
plt.figure(figsize=(10,5))
plt.plot(d_losses,label="Discriminator Loss")
plt.plot(g_losses,label="Generator Loss")
plt.title("GAN Training Performance")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
# Save Graph
plt.savefig("Exp10_Loss_Comparison.png")
plt.close()
# Analysis
print("\nAnalysis:")
print("1. GAN generates synthetic handwritten digit images.")
print("2. Generated outputs improve over training iterations.")
print("3. Generator and discriminator compete during training.")
print("4. Loss graph compares generator and discriminator performance.")
print("5. GAN may generate blurry or noisy images.")
print("6. More training improves image quality.")
print("\nTraining complete.")
print("Check folder for generated images and loss graph.")
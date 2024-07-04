pip install pillow numpy


from PIL import Image
import numpy as np

# Function to load an image and convert it to a NumPy array
def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

# Function to save a NumPy array as an image
def save_image(image_array, output_path):
    image = Image.fromarray(image_array)
    image.save(output_path)

# Function to encrypt an image using pixel manipulation
def encrypt_image(image_array, key=50):
    # Simple encryption: add a value to each pixel
    encrypted_image = (image_array + key) % 256
    return encrypted_image

# Function to decrypt an image using pixel manipulation
def decrypt_image(encrypted_image_array, key=50):
    # Simple decryption: subtract the value added during encryption
    decrypted_image = (encrypted_image_array - key) % 256
    return decrypted_image

# Main function to demonstrate encryption and decryption
def main():
    # Load the image
    image_path = 'input_image.jpg'
    image_array = load_image(image_path)

    # Encrypt the image
    key = 50
    encrypted_image_array = encrypt_image(image_array, key)
    save_image(encrypted_image_array, 'encrypted_image.png')

    # Decrypt the image
    decrypted_image_array = decrypt_image(encrypted_image_array, key)
    save_image(decrypted_image_array, 'decrypted_image.png')

    print("Encryption and decryption completed. Check the output images.")

if __name__ == "__main__":
    main()

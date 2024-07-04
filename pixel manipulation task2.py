pip install pillow

from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    np_image = np.array(image)
    
    # Encrypt the image by adding the key to each pixel value
    encrypted_image = (np_image + key) % 256
    
    # Convert back to an image and save
    encrypted_image = Image.fromarray(encrypted_image.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    np_image = np.array(image)
    
    # Decrypt the image by subtracting the key from each pixel value
    decrypted_image = (np_image - key) % 256
    
    # Convert back to an image and save
    decrypted_image = Image.fromarray(decrypted_image.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Simple Image Encryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    
    if choice.lower() not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return
    
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the output path for the processed image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))
    
    if choice.lower() == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice.lower() == 'd':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()

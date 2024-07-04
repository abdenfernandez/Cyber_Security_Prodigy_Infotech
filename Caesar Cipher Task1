def caesar_cipher_encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Algorithm")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    
    if choice.lower() not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return
    
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice.lower() == 'e':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted Message: {encrypted_text}")
    elif choice.lower() == 'd':
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted Message: {decrypted_text}")

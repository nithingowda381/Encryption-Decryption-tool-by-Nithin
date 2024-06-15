def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text.append(chr(shifted))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():

    header = """
****************************************************
*       Welcome to Nithin's Caesar Cipher Tool      *
****************************************************
    """
    print(header)

    while True:
        choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'X' to exit: ").upper()

        if choice == 'E':
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (a number between 1 and 25): "))
            encrypted_message = encrypt(plaintext, shift)
            print(f"\nEncrypted message: {encrypted_message}\n")

        elif choice == 'D':
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value used for encryption: "))
            decrypted_message = decrypt(ciphertext, shift)
            print(f"\nDecrypted message: {decrypted_message}\n")

        elif choice == 'X':
            print("Exiting the Caesar Cipher tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'X' to exit.\n")

if __name__ == "__main__":
    main()

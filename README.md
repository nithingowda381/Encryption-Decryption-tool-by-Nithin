# Caesar Cipher Tool

## Overview
This Python script implements a Caesar Cipher encryption and decryption tool. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features
- **Encryption**: Encrypts messages by shifting each letter in the plaintext forward in the alphabet by a specified number of positions.
- **Decryption**: Decrypts messages by shifting each letter in the ciphertext backward in the alphabet using the same shift value used for encryption.
- **User Interaction**: Provides a command-line interface for users to input messages, choose encryption or decryption, and specify the shift value.
- **Input Validation**: Ensures that only alphabetic characters are encrypted or decrypted, preserving non-alphabetic characters like punctuation and spaces.
- **Range Limitation**: Restricts the shift value to be between 1 and 25, corresponding to the standard alphabet length.

## Usage
1. **Run the Script**: Execute the script in a Python environment.
2. **Choose Operation**:
   - Enter 'E' to encrypt a message.
   - Enter 'D' to decrypt a message.
   - Enter 'X' to exit the tool.
3. **Encryption**:
   - Enter the message you want to encrypt.
   - Provide a shift value between 1 and 25.
   - The encrypted message will be displayed.
4. **Decryption**:
   - Enter the encrypted message.
   - Input the same shift value used for encryption.
   - The decrypted message will be shown.
5. **Exit**: Choose 'X' to exit the tool.

## Example
```
****************************************************
*       Welcome to Nithin's Caesar Cipher Tool      *
****************************************************

Enter 'E' to encrypt, 'D' to decrypt, or 'X' to exit: E
Enter the message to encrypt: Hello, World!
Enter the shift value (a number between 1 and 25): 3

Encrypted message: Khoor, Zruog!

Enter 'E' to encrypt, 'D' to decrypt, or 'X' to exit: D
Enter the message to decrypt: Khoor, Zruog!
Enter the shift value used for encryption: 3

Decrypted message: Hello, World!

Enter 'E' to encrypt, 'D' to decrypt, or 'X' to exit: X
Exiting the Caesar Cipher tool. Goodbye!
```

## Dependencies
- Python 3.x (No external libraries required)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
- **Author**: Nithin Gowda M S

---

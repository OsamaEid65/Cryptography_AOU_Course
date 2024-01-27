# Ceasar Cipher Encryption/Decryption

Ceasar Cipher is a simple encryption technique that shifts each letter of the plaintext by a fixed number of positions down or up the alphabet.

## Input

The program prompts the user to enter their plaintext and specify the encryption/decryption key.

## Process

1. **Encryption**: Each letter of the plaintext is shifted forward in the alphabet by the specified key.
2. **Decryption**: Each letter of the ciphertext is shifted backward in the alphabet by the specified key.

## Functions

### `ceasar_cipher_encrypt(plaintext, key)`

Encrypts the plaintext using the Ceasar Cipher technique with the given key.

### `ceasar_cipher_decrypt(ciphertext, key)`

Decrypts the ciphertext using the Ceasar Cipher technique with the given key.

### `bruteforce(ciphertext)`

Attempts to decrypt the ciphertext using a brute-force approach by trying all possible keys (0 to 25).

## Usage

1. Run the script.
2. Enter your plaintext.
3. Enter your encryption/decryption key.
4. The program will output the encrypted ciphertext and decrypted plaintext.
5. Optionally, you can use the `bruteforce()` function to attempt decrypting the ciphertext using all possible keys.

Enjoy encrypting and decrypting messages with the Ceasar Cipher!

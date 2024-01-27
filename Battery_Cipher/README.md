# Battery Cipher

Battery Cipher is a Python program designed to encrypt and decrypt messages using the Battery Cipher algorithm. It offers two modes of operation: Half and Even, each with specific encryption and decryption methods.

## Modes Of Operation

### 1. Half

In this mode, the plaintext is split into two halves. The characters in the first half are shifted forward by the given key, while the characters in the second half are shifted backward by the same key. The ciphertext is formed by concatenating the processed halves.

### 2. Even

This mode is suitable for plaintext with an even number of characters. The plaintext is divided into substrings of four characters each. For each substring, the first two characters are shifted forward by the key, and the last two characters are shifted backward. The resulting ciphertext is formed by concatenating these processed substrings.

## Usage

1. Run the script.
2. Enter the plaintext.
3. Enter the encryption/decryption key.
4. Choose the mode of operation (Half or Even).
5. The script will output the ciphertext or plaintext, depending on the chosen mode of operation.

## Note

- Ensure that the key provided is within the range of 1 to 24.
- Choose the appropriate mode of operation based on the plaintext length.
- Enjoy encrypting and decrypting messages with Battery Cipher!


"""
Name : Battery Cipher
Author : Osama Eid
Modes Of Operation : Half , Even
Key Range : 1 - 24
date : 25/1/2024
"""
#____INPUT____#
plaintext = input("Enter the plain text : ").lower() 
key = int(input("Enter the key : "))
if key > 26 or key < 1:
    print("Error : The key must be between 1 and 26")
    exit()
alphabet="abcdefghijklmnopqrstuvwxyz"
mode_of_operation = input("Enter the mode of operation : ").lower()

#____PROCESS____#
def battery_encrypt_half(plaintext, key):
    ciphertext = ""

    # split plaintext into two halves
    left = plaintext[:len(plaintext)//2]
    right = plaintext[len(plaintext)//2:]

    # encrypt left half
    for char in left:
        ciphertext += alphabet[(alphabet.index(char) + key) % 26]
    
    # encrypt right half
    for char in right:
        ciphertext += alphabet[(alphabet.index(char) - key) % 26]
    
    return ciphertext

def battery_decrypt_half(ciphertext, key):
    plaintext = ""

    # split plaintext into two halves
    left = ciphertext[:len(ciphertext)//2]
    right = ciphertext[len(ciphertext)//2:]

    # encrypt left half
    for char in left:
        plaintext += alphabet[(alphabet.index(char) - key) % 26]
    
    # encrypt right half
    for char in right:
        plaintext += alphabet[(alphabet.index(char) + key) % 26]
    
    return plaintext

def battery_encrypt_even(plaintext, key):
    ciphertext = ""
    
    for i in range(0, len(plaintext), 4):
        # split plaintext into two halves
        left = plaintext[i:i+2]
        right = plaintext[i+2:i+4]

        # encrypt left half
        for char in left: 
            ciphertext += alphabet[(alphabet.index(char)+key)%26]
           
        # encrypt right half
        for char in right:
            ciphertext += alphabet[(alphabet.index(char)-key)%26]

    return ciphertext

def battery_decrypt_even(plaintext, key):
    ciphertext = ""
    
    for i in range(0, len(plaintext), 4):
        # split plaintext into two halves
        left = plaintext[i:i+2]
        right = plaintext[i+2:i+4]

        # encrypt left half
        for char in left: 
            ciphertext += alphabet[(alphabet.index(char)-key)%26]
           
        # encrypt right half
        for char in right:
            ciphertext += alphabet[(alphabet.index(char)+key)%26]

    return ciphertext

#____HELPER FUNCTIONS____#
def demo():
    print("==== demo for Battery Cipher Encryption/Decryption ====")

#____OUTPUT____#
if mode_of_operation == "half":
    ciphertext = battery_encrypt_half(plaintext,key)
    demo()
    print(f"Cipher Text : {ciphertext}")
    decrypted = battery_decrypt_half(ciphertext, key)
    print(f"Plain Text : {decrypted}")

elif mode_of_operation == "even":
    ciphertext = battery_encrypt_even(plaintext,key)
    demo()
    print(f"Cipher Text : {ciphertext}")
    decrypted = battery_decrypt_even(ciphertext, key)
    print(f"Plain Text : {decrypted}")

else:
    print("Error : The mode of operation must be half or even")
    exit()

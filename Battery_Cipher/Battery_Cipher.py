<<<<<<< HEAD
"""
Name : Battery Cipher
Author : Osama Eid
Modes Of Operation : Half , Even
Key Range : 1 - 24
date : 25/1/2024
"""
import math
plain_text = input("Enter the plain text : ").lower()
key = eval(input("Enter the key : "))
alphapt="abcdefghigklmnopqrstuvwxyz"
mode_of_operation = input("Enter the mode of operation : ").lower()
def battery_cipher_encrypt_half_even_char(plain_text,key):
    if len(plain_text)%2 == 0:
        list1=list(plain_text)


        list2=list1[0:len(list1)//2]
        list3=list1[len(list1)//2:len(list1)]

        for i in range(0,len(list2)):
            list2[i]=alphapt[(alphapt.index(list2[i])+key)%26]

        for i in range(0,len(list3)):
            list3[i]=alphapt[(alphapt.index(list3[i])-key)%26]

        ciphet_text=''.join(list2+list3)
        return ciphet_text
    else:
        print("Error : The length of the plain text must be even")
        exit()
def battery_cipher_decrypt_half_even_char(cipher_text,key):
    if len(cipher_text)%2 == 0:
        list1=list(cipher_text)
        list2 = list1[0:len(list1) // 2]
        list3 = list1[len(list1) // 2:len(list1)]

        for i in range(0, len(list2)):
            list2[i] = alphapt[(alphapt.index(list2[i]) - key) % 26]

        for i in range(0, len(list3)):
            list3[i] = alphapt[(alphapt.index(list3[i]) + key) % 26]

        plain_text = ''.join(list2 + list3)
        return plain_text
def battery_cipher_encrypt_half_odd_char(plain_text,key):
    if len(plain_text)%2 != 0:
        list1=list(plain_text)
        list2=list1[0:math.ceil(len(list1)/2)]
        list3=list1[math.ceil(len(list1)/2):len(list1)]
        for i in range(0,len(list2)):
            list2[i]=alphapt[(alphapt.index(list2[i])+key)%26]
        for i in range(0,len(list3)):
            list3[i]=alphapt[(alphapt.index(list3[i])-key)%26]
        ciphet_text=''.join(list2+list3)
        return ciphet_text
    else:
        print("Error : The length of the plain text must be odd")
        exit()
def battery_cipher_decrypt_half_odd_char(cipher_text,key):
    if len(cipher_text)%2 != 0:
        list1=list(cipher_text)
        list2 = list1[0:math.ceil(len(list1)/2)]
        list3 = list1[math.ceil(len(list1)/2):len(list1)]
        for i in range(0, len(list2)):
            list2[i] = alphapt[(alphapt.index(list2[i]) - key) % 26]
        for i in range(0, len(list3)):
            list3[i] = alphapt[(alphapt.index(list3[i]) + key) % 26]
        plain_text = ''.join(list2 + list3)
        return plain_text
def battery_cipher_encrypt_even_for_even_char(plain_text,key):
    transformed_text = ""
    if len(plain_text)%2 == 0:
        list1=list(plain_text)
        for i in range(0,len(list1),4):
            list2 = list1[i:i+2]
            list3= list1[i+2:i+4]
            process_on_list2=""
            process_on_list3=""
            for char in list2:
                process_on_list2+=alphapt[(alphapt.index(char)+key)%26]
            for char in list3:
                process_on_list3+=alphapt[(alphapt.index(char)-key)%26]
            transformed_text+=process_on_list2+process_on_list3
    return transformed_text
def battery_cipher_decrypt_even_for_even_cahr(plain_text,key):
    transformed_text = ""
    if len(plain_text)%2 == 0:
        list1=list(plain_text)
        for i in range(0,len(list1),4):
            list2 = list1[i:i+2]
            list3= list1[i+2:i+4]
            process_on_list2=""
            process_on_list3=""
            for char in list2:
                process_on_list2+=alphapt[(alphapt.index(char)-key)%26]
            for char in list3:
                process_on_list3+=alphapt[(alphapt.index(char)+key)%26]
            transformed_text+=process_on_list2+process_on_list3
    return transformed_text

def Battery_cipher_encrypt_even_for_odd_char(plain_text,key):
    transformed_text = ""
    if len(plain_text)%2 != 0:
        list1=list(plain_text)
        for i in range(0,len(list1),4):
            list2 = list1[i:i+2]
            list3= list1[i+2:i+4]
            process_on_list2=""
            process_on_list3=""
            for char in list2:
                process_on_list2+=alphapt[(alphapt.index(char)+key)%26]
            for char in list3:
                process_on_list3+=alphapt[(alphapt.index(char)-key)%26]
            transformed_text+=process_on_list2+process_on_list3
    return transformed_text
def battery_cipher_decrypt_even_for_odd_char(plain_text,key):
    transformed_text = ""
    if len(plain_text)%2 != 0:
        list1=list(plain_text)
        for i in range(0,len(list1),4):
            list2 = list1[i:i+2]
            list3= list1[i+2:i+4]
            process_on_list2=""
            process_on_list3=""
            for char in list2:
                process_on_list2+=alphapt[(alphapt.index(char)-key)%26]
            for char in list3:
                process_on_list3+=alphapt[(alphapt.index(char)+key)%26]
            transformed_text+=process_on_list2+process_on_list3
    return transformed_text

if key > 24 or key < 1:
    print("Error : The key must be between 1 and 24")
    exit()
if mode_of_operation == "half":
    if len(plain_text)%2 ==0:
        Cipher_Text=battery_cipher_encrypt_half_even_char(plain_text,key)
        print(f"Cipher Text : {Cipher_Text}")
        plain_text=battery_cipher_decrypt_half_even_char(Cipher_Text,key)
        print(f"Plain Text : {plain_text}")
    else:
        Cipher_Text = battery_cipher_encrypt_half_odd_char(plain_text, key)
        print(f"Cipher Text : {Cipher_Text}")
        plain_text = battery_cipher_decrypt_half_odd_char(Cipher_Text, key)
        print(f"Plain Text : {plain_text}")
elif mode_of_operation == "even":
    if len(plain_text)%2 ==0:
        Cipher_Text=battery_cipher_encrypt_even_for_even_char(plain_text,key)
        print(f"Cipher Text : {Cipher_Text}")
        plain_text=battery_cipher_decrypt_even_for_even_cahr(Cipher_Text,key)
        print(f"Plain Text : {plain_text}")
    else:
        Cipher_Text = Battery_cipher_encrypt_even_for_odd_char(plain_text, key)
        print(f"Cipher Text : {Cipher_Text}")
        plain_text = battery_cipher_decrypt_even_for_odd_char(Cipher_Text, key)
        print(f"Plain Text : {plain_text}")
else:
    print("Error : The mode of operation must be half or even")
    exit()
=======
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
>>>>>>> af2508990418d3df0b372f547dbeae0c4bf9c8f5

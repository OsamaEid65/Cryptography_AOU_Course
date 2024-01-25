"""
Name : Battery Cipher
Author : Osama Eid
Modes Of Operation : Half , Even
Key Range : 1 - 24
date : 25/1/2024
"""
import math
plain_text = input("Enter the plain text : ")
key = eval(input("Enter the key : "))
alphapt="abcdefghigklmnopqrstuvwxyz"

def battery_cipher_encrypt_half(plain_text,key):
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
def battery_cipher_decrypt_half(cipher_text,key):
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
def battery_cipher_encrypt_even(plain_text,key):
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
def battery_cipher_decrypt_even(cipher_text,key):
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


if len(plain_text)%2 ==0:
    Cipher_Text=battery_cipher_encrypt_half(plain_text,key)
    print(f"Cipher Text : {Cipher_Text}")
    plain_text=battery_cipher_decrypt_half(Cipher_Text,key)
    print(f"Plain Text : {plain_text}")
else:
    Cipher_Text = battery_cipher_encrypt_even(plain_text, key)
    print(f"Cipher Text : {Cipher_Text}")
    plain_text = battery_cipher_decrypt_even(Cipher_Text, key)
    print(f"Plain Text : {plain_text}")

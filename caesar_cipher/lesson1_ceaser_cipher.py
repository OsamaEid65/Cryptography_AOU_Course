"""
ceaser cipher encryption     
"""
#input
plaintext = "hello"
alphapet="abcdefghijklmnopqrstuvwxyz"

#process
def ceaser_encrypt(plaintext,key):
    ciphertext=""
    
    for state in plaintext:
        ciphertext +=alphapet[(alphapet.index(state)+key)%26]
#output
    return ciphertext

def ceaser_decrypt(ciphertext,key):
    plaintext=""
    
    for state in ciphertext :
        plaintext += alphapet[(alphapet.index(state)-key)%26]
    return plaintext
      
def brutforce(ciphertext):
    for i in range (0,26) :
        dec=ceaser_decrypt(ciphertext,i)
    if dec == plaintext:
        return dec  
#main
key = 3

cipher_text=ceaser_encrypt(plaintext,key)

print(f"the ciphertext is : {cipher_text}")

plaintext= ceaser_decrypt(cipher_text,key)

print(f"the plaintext is : {plaintext}")

brutforce(cipher_text)
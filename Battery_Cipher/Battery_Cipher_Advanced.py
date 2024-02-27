import binascii
import random

def Round_Functions_Encryption(MPT_bin,Key):

    temp = ""
    for i in range(len(MPT_bin)):
        if MPT_bin[i] == Key[i]:
            temp += '0'
        else:
            temp += '1'

    result= ""

    inverse_s = ''

    for i in temp:

        if i == '0':
            inverse_s += '1'

        else:
            inverse_s += '0'

    left = temp[:len(temp) // 2]
    #new
    L_left= left[:len(left)//2]
    R_left= left[len(left)//2:]

    left=R_left+L_left
    right = temp[len(temp) // 2:]
    #new
    L_right=right[:len(right)//2]
    R_right=right[len(right)//2:]
    right=R_right+L_right

    result=right+left
    return result

def Round_Functions_Decryption(CPT_BIN,Key):
    temp = ""
    for i in range(len(CPT_BIN)):
        if CPT_BIN[i] == Key[i]:
            temp += '0'
        else:
            temp += '1'
    result = ""
    left = temp[:len(temp) // 2]

    L_left = left[:len(left) // 2]
    R_left = left[len(left) // 2:]

    left = R_left + L_left

    right = temp[len(temp) // 2:]

    L_right = right[:len(right) // 2]
    R_right = right[len(right) // 2:]

    right = R_right + L_right

    result = right + left
    inverse_s = ''

    for i in result:

        if i == '0':
            inverse_s += '1'

        else:
            inverse_s += '0'
    return result
def Binary_2_Desmial(PT_BIN):
    text = int(PT_BIN, 2)
    return text

def _XOR(L1, R1):
    temp = ""
    for i in range(len(L1)):
        if L1[i] == R1[i]:
            temp += '0'
        else:
            temp += '1'
    return temp

def Key_Generator(length):
    key = ""
    for _ in range(length):
        temp = random.randint(0, 1)
        temp = str(temp)
        key += temp
    return key

def Desmial_2_ASCII(PT):
    temp = []
    for i in PT:
        t1 = ord(i)
        temp.append(t1)
    return temp

def ASCII_2_Binary(a):
    temp = [format(i, '08b') for i in a]
    PT_Binary = "".join(temp)
    return PT_Binary

PT = "Osama Eid Said Eissa "
PT_ASCII = Desmial_2_ASCII(PT)
PT_BIN = ASCII_2_Binary(PT_ASCII)

half = len(PT_BIN) // 2
L1 = PT_BIN[:half]  # Corrected slicing
R1 = PT_BIN[half:]

m = len(L1)

K1 = Key_Generator(m)
K2 = Key_Generator(m)
K3 = Key_Generator(m)
K4 = Key_Generator(m)
K5 = Key_Generator(m)


f1 = Round_Functions_Encryption(R1,K1)
R2 = _XOR(f1, L1)
L2 = R1

f2 = Round_Functions_Encryption(R2,K2)
R3 = _XOR(f2, L2)
L3 = R2

f3= Round_Functions_Encryption(R3,K3)
R4= _XOR(f3,L3)
L4= R3

f4= Round_Functions_Encryption(R4,K4)
R5= _XOR(f4,L4)
L5= R4

f5= Round_Functions_Encryption(R5,K5)
R6= _XOR(f5,L5)
L6= R5


# Cipher Text
bin_data = L6 + R6
str_data = ''
for i in range(0, len(bin_data), 8):
    temp = bin_data[i:i + 8]
    Decimal_data = Binary_2_Desmial(temp)
    str_data += chr(Decimal_data)
CT=bytes(str_data,'utf-8')
print(f"Cipher_text=---->{CT}")

# Decryption process goes here...

D_L1 = L6
D_R1 = R6

D_F5 = Round_Functions_Decryption(D_L1,K5)
D_L2 = _XOR(D_R1,D_F5)
D_R2 = D_L1

D_F4 = Round_Functions_Decryption(D_L2,K4)
D_L3 = _XOR(D_R2,D_F4)
D_R3 = D_L2

D_F3 =Round_Functions_Decryption(D_L3,K3)
D_L4= _XOR(D_R3,D_F3)
D_R4= D_L3

D_F2 = Round_Functions_Decryption(D_L4,K2)
D_L5 = _XOR(D_R4, D_F2)
D_R5 = D_L4

D_F1 = Round_Functions_Decryption(D_L5,K1)
D_L6 = _XOR(D_R5, D_F1)
D_R6 = D_L5
PT1 = D_L6 + D_R6

PT1=int(PT1,2)
RPT = binascii.unhexlify( '%x'% PT1)
print("Retrieved Plain Text is: ", RPT)
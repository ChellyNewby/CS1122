#Richelle Newby
#rnn225

import binascii

#Converting numbers to binary

def BinaryConversion(num):
    inbin_num= bin(num)  #Converts the number to binary
    bin_num= inbin_num[2:] # Removes the 0b in the beginning

    if (len(bin_num) < 8 ):
        bin_num= ('0' * (8-len(bin_num))) + bin_num  # Adds the leading zeros

    return bin_num



print("Binary conversion for 57 is: ", BinaryConversion(57))
print("Binary conversion for 123 is: ", BinaryConversion(123))
print("Binary conversion for 85 is: ", BinaryConversion(85))
print("Binary conversion for 38 is: ", BinaryConversion(38))



#Converting strings to hexadecimal digits


def HexadecimalConversion(string):

    outstring=""
    string_lst= string.split()     #Creates a string list

    for word in string_lst: 
        word=word[2:]           #Removes 0x
        hexaword= binascii.unhexlify(word)    #Converting to string
        hexaword=hexaword.decode("utf-8")
        outstring=outstring + hexaword   #Adds the word to the final string
        
    return outstring


print (HexadecimalConversion("0x41 0x53 0x43 0x49 0x49 0x20 0x77 0x68 0x61 0x74 0x20 0x79 0x6f 0x75 0x20 0x64 0x69 0x64 0x20 0x74 0x68 0x65 0x72 0x65"))
print (HexadecimalConversion("0x39 0x41 0x4d 0x20 0x69 0x73 0x20 0x74 0x6f 0x6f 0x20 0x65 0x61 0x72 0x6c 0x79 0x20 0x66 0x6f 0x72 0x20 0x63 0x6c 0x61 0x73 0x73"))
print(HexadecimalConversion("0x43 0x6f 0x6d 0x70 0x75 0x74 0x65 0x72 0x73 0x20 0x61 0x72 0x65 0x20 0x6d 0x61 0x67 0x69 0x63"))
print(HexadecimalConversion("0x57 0x68 0x61 0x74 0x20 0x74 0x68 0x65 0x20 0x68 0x65 0x78 0x3f"))




def BinaryToHexadecimal(binstr):
    
    basetwo=int(binstr, 2)   #converts to base 2

    hexresult=hex(basetwo)  #converts to hexadecimal


    return hexresult



print(BinaryToHexadecimal("00001011101011101101111010101101"))
print(BinaryToHexadecimal("11001010111111101111101011001110"))
print(BinaryToHexadecimal("10111110111011111101000000001101"))
print(BinaryToHexadecimal("11111111111111111001000001100010"))






def OctToDecimal(num):
    result=0
    numstring= str(num)   
    n=len(numstring)-1    #finds the nth power
    
    for number in numstring:
        converted= int(number)* 8**n   #converts the number
        result+=converted
        n-=1

    return result



print(OctToDecimal(10))
print(OctToDecimal(42))
print(OctToDecimal(77))
print(OctToDecimal(113))



















        
    
     

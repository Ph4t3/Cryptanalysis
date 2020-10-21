

# This file was *autogenerated* from the file Affine.sage
from sage.all_cmdline import *   # import sage library

_sage_const_26 = Integer(26); _sage_const_1 = Integer(1); _sage_const_27 = Integer(27)
import argparse

### To encrypt a single letter
def affineEncryptLetter(letter, a, b):
    # if not an alphabet dont encrypt
    if not letter.isalpha():
        return letter
# (a*letter + b)%26
    return chr((a*(ord(letter.upper()) - ord('A')) + b)%_sage_const_26  + ord('A')) 

### To decrypt a single letter
def affineDecryptLetter(letter, a, b):
    # if not an alphabet dont decrypt
    if not letter.isalpha():
        return letter

    # (modInv(a)*(letter - b))%26
    return chr((inverse_mod(a, _sage_const_26 )*(ord(letter.upper()) - ord('A') - b))%_sage_const_26  + ord('A')) 

### To encrypt a line
def affineEncrypt(line, a, b):
    return ''.join([affineEncryptLetter(c,a,b) for c in line])

### To decrypt a line
def affineDecrypt(line, a, b):
    return ''.join([affineDecryptLetter(d,a,b) for d in line])

### generates a random element coprime to 26
def random_coprime():
    coprimes = []
    for i in range(_sage_const_1 , _sage_const_27 ):
        if gcd(i, _sage_const_26 ) == _sage_const_1 :
            coprimes.append(i)
    return coprimes[ZZ.random_element(len(coprimes))]

### Main Function
def main():
    # Arguments parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", required=True, choices=['encrypt','decrypt'], help="Encrypt or Decrypt the file")
    parser.add_argument("-a", type=int, help="Coefficient A (optional for encrypt)")
    parser.add_argument("-b", type=int, help="Coefficient B (optional for encrypt)")
    parser.add_argument("-i", "--input-file", required=True, help="Input file with plaintext or ciphertext")
    parser.add_argument("-o", "--output-file", required=True, help="Output file name")
    args = parser.parse_args()

    #if decryption Coefficient is mandatory
    if args.mode == "decrypt" and (args.a is None or args.b is None):
        print("Keys are required for Decryption")
        return

    # if Coefficient A is not given, generate random element
    if args.a is None:
        args.a = random_coprime()

    # if Coefficient B is not given, generate random element
    if args.b is None:
        args.b = ZZ.random_element(_sage_const_1 , _sage_const_27 )

    # Check if 'a' is co-prime with 26
    if gcd(args.a, _sage_const_26 ) != _sage_const_1 :
        print("Error: 'a' is not co-prime with 26")
        return
    
    inputFile = open(args.input_file, "rt")
    outputFile = open(args.output_file, "wt")
    keyFile = open("key_"+args.output_file, "wt")

    #encrypt or decrypt depending on mode flag
    if args.mode == "encrypt":
        for line in inputFile:
            outputFile.write(affineEncrypt(line, args.a, args.b))
    elif args.mode == "decrypt":
        for line in inputFile:
            outputFile.write(affineDecrypt(line, args.a, args.b))

    #write keys to keyFile
    keyFile.write("A = " + str(args.a) + "\n")
    keyFile.write("B = " + str(args.b) + "\n")

    inputFile.close()
    outputFile.close()
    keyFile.close()

if __name__ == '__main__':
    main()
### Code is written by Nikhil R

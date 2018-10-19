"""
This script takes in an encrypted Caeser Cipher and brute forces it
"""

import sys

def ceaser(text, s):
    result = ""

    for i in range (len(text)):
        char = text[i]
        
        if(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def main():
    msg = sys.argv[1]
    
    for key in range (0,  27):
        k = 26 - key
        print("Key :" + str(key))
        print(ceaser(msg, k))
        print("\n")

if __name__ == "__main__":
    main()

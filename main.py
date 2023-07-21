def encrypt_affine(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char == ' ':
            ciphertext += ' '
        else:
            x = ord(char) - 65
            ciphertext += chr(((a * x + b) % 26) + 65)
    return ciphertext

def decrypt_affine(ciphertext, a, b):
    plaintext = ""
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    for char in ciphertext:
        if char == ' ':
            plaintext += ' '
        else:
            x = ord(char) - 65
            plaintext += chr((a_inv * (x - b)) % 26 + 65)
    return plaintext

def main():
    print("-Affine Cipher encryption and decryption-")
    choice = input("Enter 1 to encrypt, 2 to decrypt, or 3 to do both: ")
    if choice == '1':
        plaintext = input("Enter plaintext: ").upper()
        a = int(input("Enter a value: "))
        a_inv = 0
        for i in range(26):
            if (a * i) % 26 == 1:
                a_inv = i
                break
        if((a_inv<1)or(not (a>=1 and a<=26))):
            print("You Should enter a number that has an inverse and less than 27")
        else:
            b = int(input("Enter b value: "))
            if((b>=1 and b<=26)):
                print("Ciphertext:", encrypt_affine(plaintext, a, b))
            else:
                print("You Should enter a number less than 27")
    elif choice == '2':
        ciphertext = input("Enter ciphertext: ").upper()
        a = int(input("Enter a value: "))
        a_inv = 0
        for i in range(26):
            if (a * i) % 26 == 1:
                a_inv = i
                break
        if((a_inv<1)or(not (a>=1 and a<=26))):
            print("You Should enter a number that has an inverse and less than 27")
        else:
            b = int(input("Enter b value: "))
            if((b>=1 and b<=26)):
                print("Plaintext:", decrypt_affine(ciphertext, a, b))
            else:
                print("You Should enter a number less than 27")
    elif choice == '3':
        plaintext = input("Enter plaintext: ").upper()
        a = int(input("Enter a value: "))
        a_inv = 0
        for i in range(26):
            if (a * i) % 26 == 1:
                a_inv = i
                break
        if((a_inv<1)or(not (a>=1 and a<=26))):
            print("You Should enter a number that has an inverse and less than 27")
        else:
            b = int(input("Enter b value: "))
            if((b>=1 and b<=26)):
                ciphertext = encrypt_affine(plaintext, a, b)
                print("Ciphertext:", ciphertext)
                print("Plaintext:", decrypt_affine(ciphertext, a, b))
            else:
                print("You Should enter a number less than 27")
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()
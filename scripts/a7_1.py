#!/usr/bin/env python

import argparse
from cryptography.fernet import Fernet


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will encrypt or decrypt a file. Pos1: Filename Pos2:if user wants to decrypt or encrypt Pos3: decrpyt required Keyfile"
    )
    parser.add_argument("fileName", action="store", help="Enter the filename")
    parser.add_argument(
        "--encrypt",
        action="store_false",
        help="Enter '--encrypt' if you want to encrypt the file",
    )
    parser.add_argument(
        "--decrypt",
        action="store_true",
        help="Enter '--decrypt' if you want to decrypt the file",
    )
    parser.add_argument(
        "-key", action="store", help="Enter the key for the decryption ex. -key keyFile"
    )
    parser.add_argument("--version", action="version", version="1.7")
    args = parser.parse_args()
    return args


def locksmith(fileName):
    # generates a key maybe in the future if the user has a key I can skip this
    key = Fernet.generate_key()
    keyName = fileName + ".key"
    with open(keyName, "wb") as key_file:
        key_file.write(key)
    print(f"Your key file is named 'lock.key'")
    return Fernet(key)


def encrpytor(fileName, key):
    # open provided file
    with open(fileName, "rb") as file:
        fileData = file.read()
    # encrypt the data
    encryptedData = key.encrypt(fileData)
    # write to file
    newName = "encrypt_" + fileName
    with open(newName, "wb") as file:
        file.write(encryptedData)
    return


def decryptor(key, encryptedFile):
    # open provided key
    with open(key, "rb") as keyFile:
        key = keyFile.read()
    # convert to fernet key
    key = Fernet(key)
    # open and read encrypted data
    with open(encryptedFile, "rb") as file:
        encryptedData = file.read()
    # decrypt the data
    decryptedData = key.decrypt(encryptedData)
    # write decrypt data to filee and new name
    newName = "decrypt_" + encryptedFile
    with open(newName, "wb") as file:
        file.write(decryptedData)
    return


def main():
    args = ArgParse_slides()
    try:
        # Catches the decrpt arguement without providing a key
        if args.decrypt and not args.key:
            print(f"Decrypt requires a key file")
        if args.decrypt == True:  # catches the true decrypt
            decryptor(args.key, args.fileName)
            print(f"Your file has been decrypted")
        if args.encrypt == False:  # catches the false encrypt
            encrpytor(args.fileName, locksmith(args.fileName))
            print(f"Your file has been encrypted")
    except:
        print("Error has occured exiting script")
        quit()


if __name__ == "__main__":
    main()

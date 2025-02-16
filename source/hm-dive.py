#!/usr/bin/env python

from cryptography.fernet import Fernet

import argparse

parser = argparse.ArgumentParser(description='Use Fernet symmetric encryption to encrypt or decrypt files')

group = parser.add_mutually_exclusive_group()

group.add_argument('-e', '--encrypt', help='encrypt a file', action='store_true')
group.add_argument('-d', '--decrypt', help='decrypt a file', action='store_true')

parser.add_argument('file', metavar='F', help='target file')
#parser.add_argument('passphrase', metavar='P', help='passphrase for encryption')

args = parser.parse_args()

key_filename = args.file.replace('.','-') + '-key.bin'

target_file = open(args.file, "rb")

if args.encrypt: 
    key = Fernet.generate_key()
    key_file = open(key_filename, "wb")
    key_file.write(key)
    key_file.close()
    fernet = Fernet(key)
    token = fernet.encrypt(target_file.read())
    target_file.close()

    target_file = open(args.file, "wb")
    target_file.write(token)

    print("Encrypted file " + args.file)

if args.decrypt:
    key_file = open(key_filename, "rb")
    key = key_file.read()
    print(key)
    key_file.close()
    fernet = Fernet(key)
    token = fernet.decrypt(target_file.read())
    target_file.close()
    target_file = open(args.file, "w")
    target_file.write(token.decode("ascii"))
    print("Decrypted file " + args.file)
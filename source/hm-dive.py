#!/usr/bin/env python

from cryptography.fernet import Fernet

import argparse

parser = argparse.ArgumentParser(description='Use Fernet symmetric encryption to encrypt or decrypt files')

group = parser.add_mutually_exclusive_group()

group.add_argument('-e', '--encrypt', help='encrypt a file', action='store_true')
group.add_argument('-d', '--decrypt', help='decrypt a file', action='store_true')

parser.add_argument('file', metavar='F', help='target file')
parser.add_argument('passphrase', metavar='P', help='passphrase for encryption')



args = parser.parse_args()
print(args)
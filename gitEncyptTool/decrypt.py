# -*- coding: utf-8 -*-

import os
import pyAesCrypt
from optparse import OptionParser

encrypt_extn = '.aes'
bufferSize = 64 * 1024

def get_encryption_key():
    return 'temp'
    
def do_decypytion(folderPath):
    key = get_encryption_key()
    for (dirpath, dirnames, filenames) in os.walk(folderPath):
        print(filenames)
        for filename in filenames:
            if filename.endswith('.aes'):
                fullpath = dirpath + '/' + filename
                unEncruptedFile = fullpath[:-4]
                pyAesCrypt.decryptFile(fullpath, unEncruptedFile, key, bufferSize)
                
                # Remove the encrypted file after encryption. Although not desired as 
                # while encrypting, the file will be over-writed, but why create the confusion eh.
                os.remove(dirpath + '\\' + filename)
        
if __name__== "__main__":
    do_decypytion(os.getcwd())
    
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
        for filename in filenames:
            if filename.endswith('.aes'):
                fullpath = dirpath + '/' + filename
                unEncruptedFile = fullpath[:-4]
                pyAesCrypt.decryptFile(fullpath, unEncruptedFile, key, bufferSize)
            
        
if __name__== "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--directory", dest="directory",
                      help="full path of the directory")
    
    (options, args) = parser.parse_args()
    
    if options.directory == None:
        parser.print_help()
    else:        
        do_decypytion(options.directory)
    
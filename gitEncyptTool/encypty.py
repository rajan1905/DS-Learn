# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
import pyAesCrypt

password = 'temp'
encrypt_extn = '.aes'
bufferSize = 64 * 1024
files_to_be_excluded = ['encypty.py' ,  'decrypt.py']

def get_github_credentials():
    print('Remove this')

def get_encryption_key():
    return password

def generate_metadata():
    print('Remove this')

def update_metadata():
    print('Remove this')
    
def do_encypytion(f_path):
    # Traverse every folder recursively in top-down fashion and perform
    # encyrption on all files except of course the files with extension
    # aes, encrypt.py
    
    for root,d_names,f_names in os.walk(f_path): 
        eligible_files = []
        
        for f in f_names:
            if not f.endswith('.aes') and f not in files_to_be_excluded:
                eligible_files.append(f)
        
        for f in eligible_files:
            abs_path = root + '\\' + f
            pyAesCrypt.encryptFile(abs_path, abs_path+'.aes', password, bufferSize)

def check_have_latest_code():
    print('Remove this')

def push_github():
    print('Remove this')    
    
def setup():
    ''' Check if the metadata file is presnt in the folder.
    If not, we can assume all files to be NORMAL state, and make metadata for it.
    If the metadata is present, check for new file added in the current folder,
    and add entries for the file in metadata. '''
    
    do_encypytion(os.getcwd())            
            
if __name__== "__main__":
  setup()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

folder_path = ''

def get_github_credentials():
    print('Remove this')

def get_encryption_key():
    print('Remove this')

def generate_metadata():
    print('Remove this')

def update_metadata():
    print('Remove this')
    
def do_encypytion():
    print('Remove this')

def check_have_latest_code():
    print('Remove this')

def push_github():
    print('Remove this')    
                
def setup():
    ''' Check if the metadata file is presnt in the folder.
    If not, we can assume all files to be NORMAL state, and make metadata for it.
    If the metadata is present, check for new file added in the current folder,
    and add entries for the file in metadata. '''
  
    for arg in sys.argv:
        if arg != '':
            folder_path = arg
            
if __name__== "__main__":
  setup()

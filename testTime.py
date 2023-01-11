#!/bin/env python3 
import os
def create_python_script(filename):
  # Start of a new Python program
  with open(filename, 'r'):
  
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("test.py"))



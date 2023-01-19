#!/bin/env python3 
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w'):
    pass

  
  timestamp = timestamp = os.path.getmtime(filename)
  datetime.datetime.fromtimestamp(timestamp)


print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
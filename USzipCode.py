#!/usr/bin/env python3import re
def check_zip_code (text):
    pattern = r"([\s][\d]{5})"
    result = re.search(pattern, text)
    return result != None
print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("12345.")) # False

import string
import random

def generate_unique_code():
    length=6
    while (True):
        code= ''.join(random.choices(string.ascii_uppercase, k = length))
        print(code)
generate_unique_code()

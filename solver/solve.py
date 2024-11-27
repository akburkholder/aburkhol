#!/usr/bin/env python3
import binascii
import random
import string

def crc16(data):
    return binascii.crc_hqx(data, 0)

password = 'this_is_a_very_secure_password'
password_crc = crc16(password.encode('utf-8')) # 27892



def generate_random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()=+<>,./?[]{}:;'
    return ''.join(random.choice(characters) for i in range(length))


while True:
    test = generate_random_string(10)
    test_crc = crc16(test.encode('utf-8'))

    if test_crc == password_crc:
        print("Found collision: ", test)
        print("Enter '"+test+"' into check_password.py to receive flag!")
        break


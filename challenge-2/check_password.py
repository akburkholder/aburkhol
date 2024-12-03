#!/usr/bin/sudo /usr/bin/python3
import binascii

def get_crc16(data):
    return binascii.crc_hqx(data, 0)

def correct_crc(data):
    
    sample_crc = get_crc16(data)
    
    # super secure crc16 of our password:
    flag_crc = 27892

    return flag_crc==sample_crc


with open("/challenge/flag.txt", "r") as file:
    flag = file.read()

while(True):
    try:
        print("If you know the correct password, you will get the flag...")
        guess = input("Enter the password: ")
        if correct_crc(guess.encode('utf-8')):
            print("Congratulations! Here is your flag:", flag, sep='\n')
            break
    except Exception as e:
        print("That is not the correct password, goodbye")
        break


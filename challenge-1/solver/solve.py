#!/usr/bin/env python3
import shutil
import base64

if __name__ == "__main__":

    # import modified jpg
    with open('puffin.jpg', 'rb') as img:
        # seek to b64 encoded data and extract
        img.seek(int(0x348de7))
        encoded = img.read()

    # decode and save as zip file 
    #(can be revealed by running 'file' on decoded data
    with open('decoded_data.zip', 'wb') as f:
        f.write(base64.b64decode(encoded))

    # unzip archive and save directory
    shutil.unpack_archive('decoded_data.zip', 'unpacked_data')
    
    # cat flag.txt
    with open('unpacked_data/flag.txt', 'r') as flag:
        print("The flag is:")
        print(flag.read())


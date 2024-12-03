# CRC Stress Test

- Namespace: picoctf/18739f24
- ID: crc-stress-test
- Type: custom
- Category: crypto
- Points: 50
- Templatable: no
- MaxUsers: 0

## Description 

Stress test the security of CRCs

check\_password.py relies on CRC16 to verify a password. Maybe we can exploit this...

## Details 

Connect to the program with netcat:
`$ nc {{server}} {{port}}`

To run {{url_for("check_password.py", "check_password.py")}} and get the flag

## Hints

- You may not be able to guess the password, but there might be another workaround 
- This CRC algorithm is prone to collisions...

## Attributes

- author: aburkhol


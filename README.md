# CRC Stess Test Walkthrough

## Overview
This problem is intended to demonstrate the dangers of relying on an easily
collidable hash (or a
checksum) as the
sole means of verifying sensitive information, such as, in this case, a
password. The player is given a script that, when run in a docker container,
will ask the player for a password to access the flag. If the password provided
by the player matches the hash of the master password, the program will print the
flag for the player. 

In particular, check\_password.py computes a CRC16 checksum over the
player-provided password. It then checks whether this value matches the checksum
computed over the password provided in solve.py, which is hard-coded in the
check\_password.py script. If the player provides the correct password -- that
is, a password whose CRC16 value matches that of the master password -- then she
will be granted the flag.

## Walkthrough
The point of this challenge is to emphasize that checksums such as CRCs are not
cryptographically secure. Moreover, the CRC used in the challenge (CRC16) is
especially weak; finding collisions can be done in short order. 
Because the player can view the contents of check\_password.py, she should
notice that the CRC16 of the master password is stored, hard-coded, in the
script. Knowing this, and knowing that CRCs can be collided, she should attempt
to brute force a string that will produce the same CRC16 checksum. 
Because the CRC algorithm used in this challege is CRC16, brute forcing such a string
should not take long -- MANY collisions exist. 

Once the player has obtained a string whose CRC16 value matches the hard-coded
value in check\_password.py, she can submit it to the script, which will print
the flag.

## Conclusion
While this problem uses a small, collision-prone CRC algorithm, the essence of
the challenge has much broader applicability. 
In particular, MD5 hashes and CRC32 checksums are used throughout the computing
world, in embedded devices, to verify file contents, etc. 
For the sake of time and simplicity, this challenge does not ask the player to
collide these more complicated hashes -- although it is possible.

Instead, the CRC16 algorithm is used to demonstrate a more general security
concept: that hashes and checksums are often used in the wild for all sorts of
verification, that some can be collided, and that one should be wary of using
collidable hashes for security purposes.


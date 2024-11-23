# Image Forensics Walkthrough

## Overview

This problem is intended to provide exposure to simple image forensics
concepts and techniques. In particular, the provided puffin.jpg image consists
of a both a jpg image and a base64-encoded ZIP archive that contains a
flag.txt, alongside other dummy files. The image was generated such that
running command-line tools such as 'file' or 'binwalk' would not reveal the 
hidden ZIP archive. Additionally, the modified image does not visually differ 
from the original. The ultimate challenge for the player is to notice the large
chunk of base64-encoded data at the end of the image file. Knowing this, the
player can then carve the encoded data from the file and decode it. Running the
'file' command on this data reveals that the decoded data is in fact a zip
file; unzipping the archive will reveal flag.txt in the resultant, unpacked
directory. 

## Modified Image Creation

Creation of the modified .jpg image was relatively straightforward upon
realizing that data appended to the end of the image (rather than prepended to
the beginning of the file, or stashed somewhere within it) would not
visually affect the image when opened with an image reader. 

However, simply compressing the data into a ZIP archive was not sufficient to
hide the flag; it would appear in plaintext in the image data, since no
additional compression on the flag itself would be done. For this reason, the
ZIP archive was subsequently base64-encoded. This both conceals the text of the
flag and provides the player a recognizable data format, provided she has had
some prior exposure to base64. 

Thus the modified image was created by: sourcing an image of a (cute puffin)
.jpg image (found at this url: 
https://www.pexels.com/photo/puffin-in-a-field-27241058/), creating a directory
containing flag.txt and some additional dummy data, compressing that
directory into a ZIP archive, base64-encoding that archive, and appending it to
the end of our puffin image. 

## Solution

A look at the solve.py will reveal one solution for retrieving the flag.
Specifically, the player might consider running something like 'strings' on the
.jpg image and realize that the final string in the file seems to be a large
chunk of base64 data. At this point, the player might simply decode this string
to reveal the resultant ZIP archive; alternatively, as I did, the player could
search for the hexadecimal offset at which the base64 string begins (to make
sure none of it was omitted in the 'strings' output). Knowing this offset, the
player can carve out the encoded data starting at the identified offset and
going to the end of the file. This carved data can now be saved as its own file
and decoded. From this point the player should run 'file' or take a look at the
magic bytes within the resultant file to understand that what remains is a ZIP
archive that can be unzipped and from which flag.txt can be retrieved. 


#WARNING LOTS OF BUGS
#usage ./encode.py <any utf-16 encoded string>
#note this has no checking whether your string is valid so it will give error if invalid data is used
import string
import base64
import sys

CUSTOM_ALPHABET="!\"#$%&'()*+,-012345689@ABCDEFGHIJKLMNPQRSTUVXYZ[`abcdefhijklmpqr"
STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
DECODE_TRANS = string.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

s=sys.argv[1]
def decode(input):
    return base64.b64decode(input.translate(DECODE_TRANS))

print decode(s).encode("utf-16")

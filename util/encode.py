#WARNING LOTS OF BUGS
#usage ./encode.py <insert any message or data here>
import string
import base64
import sys

CUSTOM_ALPHABET="!\"#$%&'()*+,-012345689@ABCDEFGHIJKLMNPQRSTUVXYZ[`abcdefhijklmpqr"
STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
DECODE_TRANS = string.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

s=sys.argv[1]

def encode(input):
    return base64.b64encode(input).translate(ENCODE_TRANS)
def decode(input):
    return base64.b64decode(input.translate(DECODE_TRANS))
c=encode(s).decode("utf-16")
print "encoded value: "
print c
print "decoded value:"
print decode(s).encode("utf-16")

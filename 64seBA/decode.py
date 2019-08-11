#!/usr/bin/env python
# shamelessly stolen from 
# https://stackoverflow.com/questions/5537750/decode-base64-like-string-with-different-index-tables
import string
import base64

STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
CUSTOM_ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
DECODE_TRANS = string.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

def encode(input):
    return base64.b64encode(input).translate(ENCODE_TRANS)

def decode(input):
    return base64.b64decode(input.translate(DECODE_TRANS))

inputString = "hAN1hTJEd7oPnTAMtlYTsz4Pp5YQnSgNpCoPszdKdRZyd3kPdzg/vg=="
decoded = decode(inputString)
print("{} ".format(decoded))


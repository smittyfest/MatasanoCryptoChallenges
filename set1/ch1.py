'''
@@@@@@@@@@@@@@@@@@@@@@@
@ Set 1 - Challenge 1 @
@@@@@@@@@@@@@@@@@@@@@@@

Convert hex to base64
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule:
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
'''
import binascii

def hex2base64(hex):
  bin = binascii.unhexlify(hex)
  return binascii.b2a_base64(bin)

def hex2bin(hex):
  return binascii.unhexlify(hex)

def bin2hex(bin):
  return binascii.hexlify(bin)

def bin2base64(bin):
  return binascii.b2a_base64(bin)

def base642bin(base64):
  return binascii.a2b_base64(base64)

def base642hex(base64):
  bin = binascii.a2b_base64(base64)
  return binascii.hexlify(bin)

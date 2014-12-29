#!/usr/bin/env python
import binascii


class Steganography:

    def __init__(self):
        pass

    def ascii_to_binary(self, text):
        return bin(int(binascii.hexlify(text), 16)).replace('0b', '')

    def binary_to_ascii(self, binary):
        binary = int(binary, 2)

        return binascii.unhexlify('%x' % binary)

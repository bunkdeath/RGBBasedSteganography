#!/usr/bin/env python
import binascii


class Steganography:

    def __init__(self, **kwargs):
        '''
        image_path      => image file path to use
        text_file_path  => text file path to integrate into image
        text            => text to integrate into image
        encryption_key  => encryption key to encrypt text
        '''
        self.image_path = None
        self.text_content = None
        self.encryption_key = None
        self.text_file_path = None

        if kwargs.get('image_path'):
            self.set_image_path(kwargs.get('image_path'))

        if kwargs.get('text_file_path'):
            self.set_text_file_path(kwargs.get('text_file_path'))

        if kwargs.get('text'):
            self.set_text(kwargs.get('text'))

        if kwargs.get('encryption_key'):
            self.encryption_key = kwargs.get('encryption_key')

    def ascii_to_binary(self, text):
        return bin(int(binascii.hexlify(text), 16)).replace('0b', '')

    def binary_to_ascii(self, binary):
        return binascii.unhexlify('%x' % int(binary, 2))

    def set_image_path(self, image_path):
        self.image_path = image_path

    def set_text_file_path(self, text_file_path):
        self.set_text(open(text_file_path).read())

    def set_text(self, text):
        self.text_content = text

    def set_encryption_key(self, encryption_key):
        self.encryption_key = encryption_key

    def __str__(self):
        return "%s %s %s %s " % (self.image_path, self.text_content, self.encryption_key, self.text_file_path)

    def __unicode__(self):
        return self.__str__()

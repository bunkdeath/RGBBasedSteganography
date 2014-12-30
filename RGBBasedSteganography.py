#!/usr/bin/env python
import binascii
from PIL import Image
import numpy
import os


class RGBBasedSteganography:

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
        if not os.path.exists(image_path):
            raise IOError(
                "Filename '%s' not found. Please pass valid path." %
                image_path)

        self.image_path = image_path

    def set_text_file_path(self, text_file_path):
        if not os.path.exists(text_file_path):
            raise IOError(
                "Filename '%s' not found. Please pass valid path." %
                text_file_path)

        self.set_text(open(text_file_path).read())

    def set_text(self, text):
        self.text_content = text

    def set_encryption_key(self, encryption_key):
        self.encryption_key = encryption_key

    def __pixel_to_rgb(self):
        pass

    def __set_bit_value(self, color_code, bit_value):
        bit_value = int(bit_value)
        even = (color_code % 2) == 0
        if even and bit_value == 1:
            return (color_code + 1)

        elif not even and bit_value == 0:
            return int(color_code - 1)

        return color_code

    def __pre_check(self):
        return True

    def encrypt(self):

        binary_converted_text = self.ascii_to_binary(self.text_content)
        binary_text_length = '{0:032b}'.format(len(binary_converted_text))

        binary_conversion = binary_text_length + binary_converted_text

        binary_list = list(binary_conversion)
        binary_list.reverse()

        image = Image.open(self.image_path)
        width, height = image.size
        r, g, b = numpy.array(image).T

        if not self.__pre_check():
            raise("text too large")

        for i in range(width):
            for j in range(height):
                try:
                    r[i][j] = self.__set_bit_value(r[i][j], binary_list.pop())
                    g[i][j] = self.__set_bit_value(g[i][j], binary_list.pop())
                    b[i][j] = self.__set_bit_value(b[i][j], binary_list.pop())
                except IndexError:
                    break

        im = Image.fromarray(numpy.dstack([item.T for item in (r, g, b)]))
        im.save('./images/output.png')

    def decrypt(self, image_path):
        image = Image.open(image_path)
        width, height = image.size
        r, g, b = numpy.array(image).T

        bit_from_image = ""
        bit_length = 32
        checking_for_binary_text = False

        for i in range(width):
            for j in range(height):
                bit_from_image += str(r[i][j] % 2)
                bit_from_image += str(g[i][j] % 2)
                bit_from_image += str(b[i][j] % 2)

                if bit_length <= len(bit_from_image):

                    if not checking_for_binary_text:
                        checking_for_binary_text = True

                        text_length_in_binary = bit_from_image[:bit_length]

                        bit_from_image = bit_from_image[bit_length:]
                        text_length = int('0b%s' % text_length_in_binary, 2)
                        bit_length = text_length
                    else:
                        bit_from_image = bit_from_image[:bit_length]
                        return self.binary_to_ascii(bit_from_image)

    def __str__(self):
        return "%s %s %s %s " % (self.image_path, self.text_content,
                                 self.encryption_key, self.text_file_path)

    def __unicode__(self):
        return self.__str__()

#!/usr/bin/env python
#coding:utf-8

import sys
import math

sys_version = float(sys.version[:3])

class HashUtils:

    def __init__(self):
        pass

    def rstr2binl(self, data):
        """
        convert a raw string to an array of little-endian words
        Characters > 255 have their high-byte silently ignored.
        :param data: a raw string, such as '123456'
        :return: an array of little-endian words, such as [875770417, 13877]
        """
        output = [0 for i in range((len(data) * 8) >> 5)]
        output.append(0)
        print output
        for i in range(0, len(data) * 8, 8):
            print i
            output[i >> 5] |= (ord(data[i/8]) & 0xFF) << (i % 32)
        return output

    def binl2str(self, data):
        """
        Convert an array of little-endian words to a string
        :param data: an array of little-endian words, such as [875770417, 13877]
        :return: a raw string, such as '123456'
        """
        output = ''
        for i in range(0, len(data) * 32, 8):
            output += chr(data[i >> 5] >> (i % 32) & 0xFF)
        return output

    def rstr2any(self, data, encoding):
        divisor = len(encoding)
        remainders = []
        ceil = int(math.ceil(len(data) / 2))
        dividend = [(ord(data[i*2]) << 8) | (ord(data[i*2+1])) for i in range(ceil)]

        while len(dividend) > 0:
            quotient = []
            x = 0
            for j in range(len(dividend)):
                x = (int(x) << 16) + dividend[j]
                q = math.floor(x / divisor)
                x -= q * divisor
                if len(quotient) > 0 or q > 0:
                    quotient.append(q)

            remainders.append(x)
            dividend = quotient

        return ''.join([encoding[int(remainders[i])] for i in range(len(remainders)-1, 0, -1)])

    def sha256(self, data, encoding):
        if sys_version >= 2.5:
            import hashlib
            hashfunc = hashlib.sha256
        else:
            from Crypto.Hash import SHA256
            hashfunc = SHA256.new

        return self.rstr2any(hashfunc(data).digest(), encoding)



if __name__ == '__main__':
    util = HashUtils()
    print util.rstr2binl("123456")
    print util.binl2str([875770417, 13877])


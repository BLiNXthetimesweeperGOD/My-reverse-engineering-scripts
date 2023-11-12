#A library built around the struct module which makes packing/unpacking stuff in little endian easier
import struct

#First, the pack command
#Create unsigned byte
def pbyte(number):
    byt = struct.pack("<B", number)
    return byt
#Create signed byte
def psbyte(number):
    byt = struct.pack("<b", number)
    return byt
#Create unsigned short
def pshort(number):
    short = struct.pack("<H", number)
    return short
#Create signed short
def psshort(number):
    short = struct.pack("<h", number)
    return short
#Create unsigned 32-bit integer
def pint(number):
    integer = struct.pack("<I", number)
    return integer
#Create signed 32-bit integer
def psint(number):
    integer = struct.pack("<i", number)
    return integer
#Create Float
def pfloat(number):
    Float = struct.pack("<f", number)
    return Float

#Now the inverse
#Unpack unsigned byte
def upbyte(number):
    byt = struct.unpack("<B", number)[0]
    return byt
#Unpack signed byte
def upsbyte(number):
    byt = struct.unpack("<b", number)[0]
    return byt
#Unpack unsigned short
def upshort(number):
    short = struct.unpack("<H", number)[0]
    return short
#Unpack signed short
def upsshort(number):
    short = struct.unpack("<h", number)[0]
    return short
#Unpack unsigned 32-bit integer
def upint(number):
    integer = struct.unpack("<I", number)[0]
    return integer
#Unpack signed 32-bit integer
def upsint(number):
    integer = struct.unpack("<i", number)[0]
    return integer
#Unpack Float
def upfloat(number):
    Float = struct.unpack("<f", number)[0]
    return Float

#Convert byte string to bit list (each byte being converted into a string of bits)
def bstring(byte_string):
    bit_list = []
    for byte in byte_string:
        byte_int = int.from_bytes(byte, 'big')
        bit_string = format(byte_int, '#08b')
        bit_string = bit_string[2:]
        bit_list.append(bit_string)
    return bit_list

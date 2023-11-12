#A library built around the struct module which makes packing/unpacking stuff in little endian easier
import struct

#First, the pack command
#Create unsigned byte
def bpbyte(number):
    """Packs a byte with struct (Big Endian). Usage:
bpbyte(number)"""
    byt = struct.pack(">B", number)
    return byt
#Create signed byte
def bpsbyte(number):
    """Packs a signed byte with struct (Big Endian). Usage:
bpsbyte(number)"""
    byt = struct.pack(">b", number)
    return byt
#Create unsigned short
def bpshort(number):
    """Packs a short with struct (Big Endian). Usage:
bpshort(number)"""
    short = struct.pack(">H", number)
    return short
#Create signed short
def bpsshort(number):
    """Packs a signed short with struct (Big Endian). Usage:
bpsshort(number)"""
    short = struct.pack(">h", number)
    return short
#Create unsigned 32-bit integer
def bpint(number):
    """Packs an integer with struct (Big Endian). Usage:
bpint(number)"""
    integer = struct.pack(">I", number)
    return integer
#Create signed 32-bit integer
def bpsint(number):
    """Packs a signed integer with struct (Big Endian). Usage:
bpsint(number)"""
    integer = struct.pack(">i", number)
    return integer

#Now the inverse
#Unpack unsigned byte
def bupbyte(number):
    """Unpacks a byte with struct (Big Endian). Usage:
bupbyte(number)"""
    byt = struct.unpack(">B", number)[0]
    return byt
#Unpack signed byte
def bupsbyte(number):
    """Unpacks a signed byte with struct (Big Endian). Usage:
bupsbyte(number)"""
    byt = struct.unpack(">b", number)[0]
    return byt
#Unpack unsigned short
def bupshort(number):
    """Unpacks a short with struct (Big Endian). Usage:
bupshort(number)"""
    short = struct.unpack(">H", number)[0]
    return short
#Unpack signed short
def bupsshort(number):
    """Unpacks a signed short with struct (Big Endian). Usage:
bupsshort(number)"""
    short = struct.unpack(">h", number)[0]
    return short
#Unpack unsigned 32-bit integer
def bupint(number):
    """Unpacks an integer with struct (Big Endian). Usage:
bupint(number)"""
    integer = struct.unpack(">I", number)[0]
    return integer
#Unpack signed 32-bit integer
def bupsint(number):
    """Unpacks a signed integer with struct (Big Endian). Usage:
bupsint(number)"""
    integer = struct.unpack(">i", number)[0]
    return integer

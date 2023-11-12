#Structure generator/parser functions
import os
from SimpleFileLibrary.Numbers import *

#For generating simple file headers.
#The contents of data1-data3 can be used for whatever you want as long as they're integers.
def generate_file_header(magic, data1, data2, data3):
    header = magic[0:4].encode("UTF-8")
    header +=pint(data1)
    header +=pint(data2)
    header +=pint(data3)
    return header

#For tables of files that only rely on size
def generate_size_table(count, data):
    table = pint(count)
    for i in data:
        table+=pint(os.path.getsize(i))
    for i in data:
        f = open(i, "r+b")
        table+=f.read(os.path.getsize(i))
    return table

#For tables of files with offsets to the said files, starts with a base offset.
def generate_pointer_table(count, base):
    table = pint(count) #Pack an integer. upint does the opposite. This is the file count.
    table+= pint(base) #The first pointer
    for i in range(count-1):
        base+=os.path.getsize(data[i]) #Add the size of the current file to the base offset to generate the offset of the next file
        table+=pint(base) #Pack the integer and add it to the table
    #Files get added to the output by another function (generate_file_chunk)
    return table

#For tables of files that are just the files with length info before each file (alongside a file count)
def generate_file_table(count, data):
    table = pint(count)
    for i in range(count):
        size=os.path.getsize(data[i])
        table+=pint(size)
        f = open(data[i])
        table += f.read(size)
    return table

#For generating tables that contain filenames, pointers and sizes all in one. width is the longest a filename can be.
def generate_mixed_table(count, names, width, startoff):
    table = b''
    offset = 0
    for name in names:
        size=os.path.getsize(name)
        
        basename=os.path.basename(name).encode("utf-8")
        while len(basename)-1 != width:
            basename+=b'/x00'
        table+=basename
        table+=size
            
        
#For generating lists of file names used in stuff like packages. Width is the max length of a name (and the alignment variable).
def generate_name_list(count, data, width):
    table = pint(count)
    table += pint(width)
    table = table+b'\x00\x00\x00\x00\x00\x00\x00\x00' #Pad it out a little to keep things aligned
    for file in data:
        name = os.path.basename(file).encode("UTF-8")#+b'.'#+(os.path.splitext(file)[1].encode("UTF-8"))
        while len(name) < width:
            name+=b'\x00'
        table += name
    return table

#For generating lists of file names without extensions (for making formats that rely on separate extension lists) (NOT READY)
def generate_name_list_extensionless(count, data, width):
    table = pint(count)
    table += pint(width)
    table = table+b'\x00\x00\x00\x00\x00\x00\x00\x00' #Pad it out a little to keep things aligned
    for file in data:
        name = os.path.basename(file).encode("UTF-8")
        while len(name) < width:
            name+=b'\x00'
        table += name

#The decoders
#For decoding the simple headers
def parse_file_header(head):
    magic = head[0:4].decode("UTF-8")
    data1 = upint(head[4:8])
    data2 = upint(head[8:12])
    data3 = upint(head[12:16])
    return magic, data1, data2, data3

#For decoding size tables
def parse_size_table(count, data):
    table = pint(count)
    for i in range(count):
        table+=pint(os.path.getsize(data[i]))
    return table

#Decodes all pointer table types starting at the offset given in the file.
def get_table_info(file, offset, ttype):
    fileinfo = []
    if ttype != 2: #Table type 2 is a bit too different to mix with this one...
        with open(file, "r+b") as f:
            f.seek(offset)
            count = upint(f.read(4))
            if ttype == 1: #Some tables don't have a "base" offset and just rely on a count
                base = upint(f.read(4))
                fileinfo.append(base)
            for i in range(count):
                fileinfo.append(upint(f.read(4))) #Get the pointers
        return fileinfo
    if ttype == 2:
        A = ""
        with open(file, "r+b") as f:
            f.seek(offset)
            count = upint(f.read(4))
            namelen = upint(f.read(4))
            padding = f.read(4)
            for i in range(count):
                name = f.read(namelen)
                for i in range(namelen-1):
                    A = name[i]
                    if A == b'\x00':
                        name = name[0:i-1]
                        break
                file_offset = upint(f.read(4))
                file_size = upint(f.read(4))
                padding = f.read(4)
                info = file_name, file_offset, file_size
                fileinfo.append(info)
        return fileinfo
                
            
def bit_split(byte):
    # Use bitwise right shift and AND operations to get the first 4 bits
    first_4_bits = (byte >> 4) & 0b1111
    # Use bitwise AND operation to get the last 4 bits
    last_4_bits = byte & 0b1111
    # Convert the bits to integers using the int function with base 2
    first_4_bits_int = int(bin(first_4_bits), 2)
    last_4_bits_int = int(bin(last_4_bits), 2)
    # Return a tuple of the converted integers
    return (first_4_bits_int, last_4_bits_int)

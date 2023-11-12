#A bunch of functions for managing bytes/bits.

#Convert byte string to bit string (with padding!)
def bstring_merged(byte_string):
    bit_list = []
    for byte in byte_string:
        byte_int = int.from_bytes(byte, 'big')
        bit_string = format(byte_int, '#08b')
        bit_string = bit_string[2:]
        bit_list.append(bit_string)
    bit_string = ''.join(bit_list)
    return bit_string
#Convert byte string to bit list (each byte being converted into a string of bits with padding)
def bstring(byte_string):
    bit_list = []
    for byte in byte_string:
        byte_int = int.from_bytes(byte, 'big')
        bit_string = format(byte_int, '#08b')
        bit_string = bit_string[2:]
        bit_list.append(bit_string)
    return bit_list

#Not exactly needed, but this should do the inverse of the previous function (bits to bytes)
def bstring_reverse(bstring):
    byte_list = []
    for bit_string in bstring:
        byte_int = int(bit_string, 2)
        byte = byte_int.to_bytes(1, 'big')
        byte_list.append(byte)
    byte_string = b''.join(byte_list)
    return byte_string

#Index checks

#Index check for singular bit string
def bstring_check_1(bit_string, index, value):
    bit = bit_string[index]
    if bit == value:
        return True
    if bit != value:
        return False
    return "It broke..." #Shouldn't ever end up getting returned
#Index check for bit string within a bit list
def bstring_check_2(bit_list, list_index, bit_index, value):
    bit = bit_list[list_index][bit_index]
    if bit == value:
        return True
    if bit != value:
        return False
    return "It broke..." #Shouldn't ever end up getting returned

#For CPU instructions. Specifically, ones with 4 bits assigned to the registers.
#It flips them. Register 2 gets put in place of register 1, then the bit string
#gets rebuilt.
def registerFlipper(bit_string, start_of_register_1, start_of_register_2):
    string_1 = bit_string[0:start_of_register_1-1]
    if start_of_register_2-start_of_register_1 != 4:
        string_2 = bit_string[start_of_register_1+4:start_of_register_2-1]
        if len(bit_string)-1 != start_of_register_2+4
            string_3 = bit_string[start_of_register_2+4:len(bit_string)-1]
    if len(bit_string)-1 != start_of_register_2+4
        string_3 = bit_string[start_of_register_2+4:len(bit_string)-1]
    register1 = bit_string[start_of_register_1:start_of_register_1+4]
    register2 = bit_string[start_of_register_2:start_of_register_2+4]
    

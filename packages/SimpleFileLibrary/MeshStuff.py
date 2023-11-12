import numbers
#Functions for parsing model data
import struct
#Convert individual vertices at the specified offset in the given file
def get_vertex_float(offset, file): #I've never seen a game that only has floats and no padding, but there might be one
    with open(file, "rb") as f:
        f.seek(offset)
        X = upfloat(f.read(4))
        Y = upfloat(f.read(4))
        Z = upfloat(f.read(4))
        vertex = X, Y, Z
        offset2 = f.tell()
    return offset2, vertex
def get_vertex_float_padding(offset, file): #The most common vertex type
    with open(file, "rb") as f:
        f.seek(offset)
        X = upfloat(f.read(4))
        Y = upfloat(f.read(4))
        Z = upfloat(f.read(4))
        f.seek(4, 1) #Skip the padding data
        vertex = X, Y, Z
        offset2 = f.tell()
    return offset2, vertex
def get_vertex_short(offset, file): #Frequently used on old systems (PS1, GBA)
    with open(file, "rb") as f:
        f.seek(offset)
        X = upsshort(f.read(2))
        Y = upsshort(f.read(2))
        Z = upsshort(f.read(2))
        vertex = X, Y, Z
        offset2 = f.tell()
    return offset2, vertex
def get_vertex_short_padding(offset, file): #Frequently used on old systems (PS1, GBA)
    with open(file, "rb") as f:
        f.seek(offset)
        X = upsshort(f.read(2))
        Y = upsshort(f.read(2))
        Z = upsshort(f.read(2))
        f.seek(2, 1) #Skip the padding data
        vertex = X, Y, Z
        offset2 = f.tell()
    return offset2, vertex

#Convert triangle lists/data into a usable format
def get_triangles(data):
    "" #Not implemented yet
def get_quads(data):
    "" #Not implemented yet
def get_triangles_from_strip(offset, face_count, file):
    with open(file, "rb") as f:
        f.seek(offset)
        face_list = []
        strip = struct.unpack('<' + str(face_count) + 'H', f.read(2 * face_count))
        for face in range(face_count - 2):
            f1, f2, f3 = \
                strip[(face + 0)], \
                strip[(face + 1)], \
                strip[(face + 2)]
            if face & 1:
                face_list.append((f1, f2, f3))
            else:
                face_list.append((f2, f1, f3))
        offset2 = f.tell()
    print(hex(offset2))
    return face_list, offset2

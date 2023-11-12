import struct
import os
from tkinter import filedialog as fd
FILES = fd.askopenfilenames()
infos = []
for file in FILES:
    f = open(file, "r+b")
    FLDR = file.split("/")
    FLDR = str(FLDR[len(FLDR)-1].split(".")[0])+"\\"
    magic = str(f.read(4)).split("\\")[0].replace("b'", "")
    texnum = struct.unpack("<I", f.read(4))[0]
    headlen = struct.unpack("<I", f.read(4))[0]
    padding = f.read(4)
    path = str(str(os.getcwd())+"\\"+"MIT"+"\\"+FLDR)
    print(path)
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except:
        print("Path exists, skipping creation...")
    for i in range(texnum):
        title = str(f.read(0x28)).split("\\")[0].replace("b'", "")
        offset = struct.unpack("<I", f.read(4))[0]+headlen
        size = struct.unpack("<I", f.read(4))[0]
        info = [title, offset, size]
        infos.append(info)
    for tex in infos:
        g = open(path+tex[0], "w+b")
        f.seek(tex[1])
        test = f.read(4)
        if test != b'DDS ':
            f.seek(int(tex[1]))
        f.seek(-4, 1)
        data = f.read(tex[2])
        g.write(data)
        g.flush()
        g.close()
    infos = []

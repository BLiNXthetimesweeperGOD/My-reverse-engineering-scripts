import struct
import os
from tkinter import filedialog as fd
padding = b'\x00\x00\x00\x00'
folder = fd.askdirectory()
listd = []
files = os.listdir(folder)
f = open(folder+".mit","w+b")
f.write(b'MIT\x00')
fcount = struct.pack("<I", len(files))
hsize = struct.pack("<I", len(files)*0x30+0x10)
f.write(fcount)
f.write(hsize)
f.write(padding)
offset = 0
print(folder+".mit")
for file in files:
    bfile = file.encode('UTF-8')
    while len(bfile) != 0x28:
        bfile = bfile+b'\x00'
    flength=os.path.getsize(folder+"/"+file)
    print(flength)
    infos = [folder+"/"+file, bfile, offset, flength]
    listd.append(infos)
    f.write(bfile)
    f.write(struct.pack("<I", offset))
    f.write(struct.pack("<I", flength))
    offset+=flength
for info in listd:
    g = open(info[0], "r+b")
    f.write(g.read(info[3]))
g.close()
f.close()

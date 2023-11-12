import struct
import os
from tkinter import filedialog as fd
F = fd.askopenfilename()
#F2 = fd.askopenfilenames()
f = open(F, "r+b")
#PETZ DOGZ/CATZ 2 PACKAGES (WII)
FCT = struct.unpack(">I",f.read(4))[0]
f.seek(0x10)
FNAM = F.split("/")
FNAM = FNAM[len(FNAM)-1]
print(FNAM)
tracks = []
START = []
os.mkdir(os.getcwd()+FNAM+"_unpacked")
for i in range(FCT):
    NM = str(f.read(0x10))
    NM2 = str(f.read(0x4))
    NM = NM.split("'")[1]
    NM = NM.split("\\")[0]
    NM2 = NM2.split("'")[1]
    NM2 = NM2.split("\\")[0]
    NAME = NM+"."+NM2
    FZ = struct.unpack(">I",f.read(4))[0]
    FL = struct.unpack(">I",f.read(4))[0]
    f.read(4)
    print(NAME, hex(FZ), hex(FL))

import struct
import os
from tkinter import filedialog as fd
import zlib
files = fd.askopenfilenames()
INVALID = False

for file in files:
    name = os.path.basename(file).split(".")[0]
    if not os.path.exists(os.getcwd()+"/OUTPUT/"+name+"/"):
        os.makedirs(os.getcwd()+"/OUTPUT/"+name+"/")
    outPath = os.getcwd()+"/OUTPUT/"+name+"/"
    with open(file, "rb") as f:
        fileString = f.read(4).decode("UTF-8")
        if fileString != "HOT ":
            INVALID = True
            break
        headerInfo = struct.unpack('<IIIIIIII',f.read(0x20))
        fileOverallSize = headerInfo[3]
        fileNameTableStart = headerInfo[4]
        fileCount = headerInfo[5]
        off = f.tell()
        fileList = []
        f.seek(fileNameTableStart-1)
        for i in range(fileCount):
            fn = ""
            
            A = f.read(1)
            
            while A != 0:
                A = f.read(1)[0]
                if A != 0:
                    fn+=chr(A)
            while A == 0:
                A = f.read(1)[0]
            if len(fn) != 0:
                fileList.append(fn)
                print(fn)
            f.seek(-2,1)
        for i in range(fileCount):
            f.seek(off)
            fileInfo = struct.unpack('<IIIIIIII',f.read(32))
            headSize = fileInfo[0]
            headOffset = fileInfo[1]
            fileSize = fileInfo[2]
            fileOffset = fileInfo[4]
            off = f.tell()
            f.seek(headOffset)
            if name.lower() == "textures":
                DATA1 = f.read(headSize-0x30)
                f.seek(1,1)
                DATA1_2 = b'\x00'
                DATA1_3 = f.read(0x2F)
                DATA1 = DATA1+DATA1_2+DATA1_3
            else:
                DATA1 = f.read(headSize)
            f.seek(fileOffset)
            DATA2 = f.read(fileSize)
            if name.lower() == "modelsandanims":
                DATA = DATA1+DATA2
                DATA1 = zlib.decompress(DATA)
                print("decompressed")
            if name.lower() == "world":
                DATA = DATA1+DATA2
                DATA1 = zlib.decompress(DATA)
                print("decompressed")
            with open(outPath+fileList[i], "w+b") as o:
                o.write(DATA1)
                if name.lower != "modelsandanims" and name.lower != "world":
                    o.write(DATA2)
if INVALID == True:
    print("Not a documented/supported file.\nIf this file is a package, please tell me and I'll try to work on it.")

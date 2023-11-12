import struct
import os
from tkinter import filedialog as fd
import zlib
files = fd.askopenfilenames()
INVALID = False
start = 0x80

for file in files:
    fileID = 0
    name = os.path.basename(file).split(".")[0]
    if not os.path.exists(os.getcwd()+"/OUTPUT/"+name+"/"):
        os.makedirs(os.getcwd()+"/OUTPUT/"+name+"/")
    outPath = os.getcwd()+"/OUTPUT/"+name+"/"
    with open(file, "rb") as f:
        fileString = f.read(4)
        headerInfo = struct.unpack('<IIIIIIII',f.read(0x20))
        fileTableSize = headerInfo[0]
        fileCount = headerInfo[2]
        f.seek(start)
        off = f.tell()
        startOfFiles = fileTableSize*16+0x80
        for i in range(fileTableSize):
            f.seek(off)
            fileInfo   = struct.unpack('<IIIII',f.read(20))
            f.seek(-4,1)
            fileOffset = fileInfo[0]+startOfFiles
            fileSize   = fileInfo[4]-fileInfo[0]
            thing = fileInfo[1]
            fileThing1 = fileInfo[2]
            fileThing2 = fileInfo[3]
            A = f.tell()
            off = f.tell()
            if fileSize > int(25000) and fileThing1 != 0 and fileThing2 != 0:
                f.seek(fileOffset)
                if thing != 0x5C36:
                    data = f.read(fileSize)
                    with open(outPath+"output_"+str(hex(fileOffset)).split("x")[1]+".bin", "w+b") as o:
                        o.write(data)
                        print(hex(A), hex(fileOffset))
                else: #Convert sounds to wav
                    wavInfo = struct.unpack('<IIHHIBBBBI',f.read(24))
                    wavLength = wavInfo[0]-24
                    wavChannels = wavInfo[3]
                    wavFrequency = wavInfo[4]
                    wavWidth = wavInfo[5]
                    samps = f.read(wavLength)
                    data = b'RIFF'+struct.pack("<I",wavLength)+b'WAVEfmt '+struct.pack("<I",wavWidth)+b'\x01\x00'+struct.pack("<H",wavChannels)+struct.pack("<I",wavFrequency)+b'\x00\x00\x00\x00'+struct.pack("<H",(wavChannels+1)*2)+struct.pack("<H",wavWidth)+b'data'+struct.pack("<I",wavLength)+samps
                    with open(outPath+"output_"+str(hex(fileOffset)).split("x")[1]+".wav", "w+b") as o:
                        o.write(data)
                        print(hex(A), hex(fileOffset))
                fileID+=1
if INVALID == True:
    print("Not a documented/supported file.\nIf this file is a package, please tell me and I'll try to work on it.")

#A script for unpacking/decoding everything in Rubik's World (on both DS and Wii) (Wii might need another script to handle shared file formats)

import os #Used to create our output folders
from SimpleFileLibrary.all import * #Import the simple file library (just lowers how much typing is needed here. Feel free to use it if you want to.)

#Open the files (this creates a list of files for the upcoming loop)
opened_files = open_files()

#Run a loop that goes through every input file
for file in opened_files:
    infoTable = []
    #Not Implemented check
    NI = 0
    #Get the extension an use that as our "fileType"
    filePath = os.path.splitext(file)[0]
    fileType = os.path.splitext(file)[1]
    #print(fileType)
    basepath = os.getcwd()+f"/Unpacked/{fileType}/"+os.path.splitext(os.path.basename(file))[0]
    folderName = os.path.split(file)[0].split("/")
    folderName = folderName[len(folderName)-1]
    basepathfolder = os.getcwd()+f"/Unpacked/{fileType}/"+folderName
    name = os.path.splitext(os.path.basename(file))[0]
    sizeofFile = os.path.getsize(file)
    #Exclude files that store their names in their headers!
    if fileType != ".ema" and fileType != ".eso":
        if os.path.exists(basepath) != True:
            os.makedirs(basepath)

    #Open the file
    with open(file, "r+b") as f:
        #Each file is handled based off of the extension.
        #Rubik's World has a lot of file extensions.
        
        #Text/string file
        if fileType == ".bin":
            with open(basepath+"/"+f"{name}.txt", "w+", encoding = "utf-16") as o:
                confirm = f.read(4)

                #If the start of the file is what it should be, convert the file
                if confirm == b'\x08\x00\x65\x6E':
                    ""
                    f.seek(0x12)
                    stringCount = upshort(f.read(2))
                    f.seek(4, 1)
                    pos = 0
                    while pos < sizeofFile:
                        pos = f.tell()
                        letters = upshort(f.read(2))-1
                        check = f.read(2)
                        if check[1] != 0:
                            #f.read(2)
                            ""
                        if check[1] == 0 and check[0] > 0x20:
                            f.seek(-2, 1)
                            try:
                                string = f.read(letters*2).decode("UTF-16")
                                o.write(string+"\n")
                                print(string)
                                f.read(2)
                            except:
                                f.seek(pos+4)

                #If the start of the file isn't what it should be, quit before trying to convert it
                if confirm != b'\x08\x00\x65\x6E':
                    quit()

        #Material file
        if fileType == ".ema":
            #Create the folder here since this is the only time it's needed
            if os.path.exists(basepathfolder) != True:
                os.makedirs(basepathfolder)
            #Get the name size
            nameSize = upshort(f.read(2))-1
            materialName = f.read(nameSize).decode("utf-8")
            f.seek(1)
            with open(basepathfolder+f"/{materialName}.txt", "w+") as o:
                o.write(materialName+"\n")
                for i in range(0x18): #Try to figure this info out and properly parse it
                    o.write(str(f.read(1)[0])+" ")
                
                    
                    
        
        #DS XM List
        if fileType == ".dsxml":
            #Get the name count
            count = upint(f.read(4))
            #Go through the file and get all of the names
            for i in range(count):
                soundNameSize = upshort(f.read(2))
                soundName = f.read(soundNameSize).decode("utf-8")
                print(soundName)

        #DS XM package
        if fileType == ".dsxmp":
            
            #Create some lists and variables for later
            soundNames = []
            sounds = []
            
            baseOffset = 0x3C #Jump to here after getting all of the pointers/info
            
            #Open the list file to get the names
            with open(filePath+".dsxml", "r+b") as r:
                count = upint(r.read(4)) #Used again later for the package file
                for i in range(count):
                    soundNameSize = upshort(r.read(2))
                    soundName = r.read(soundNameSize).decode("utf-8")
                    print(soundName)
                    #Add the name to the list
                    soundNames.append(soundName)
            unknown = f.read(4)
            soundChunkLength = upint(f.read(4))
            soundDataInfo = upint(f.read(4))
            soundDataInfoLength = upint(f.read(4))
            for i in range(count):
                song = upint(f.read(4))
                sounds.append(song)
            index = 0
            index2 = 1
            #Samples start at offset 0xC3. Jump to here for the sound chunk.
            f.seek(baseOffset)
            
            #Open the first output file (stores the samples, sounds and other audio-related stuff)
            with open(basepath+"/sounds.bin", "w+b") as o:
                data = f.read(soundChunkLength) #Figure out a way to split the sound chunk up into multiple files and get the looping information
                o.write(data)
            
            #Go through the list of sequences and extract them from the package
            for song in sounds:
                f.seek(song)
                songName = soundNames[index]
                with open(basepath+f"/{songName}", "w+b") as o:
                    try:
                        data = f.read(sounds[index2]-song)
                    except:
                        data = f.read(sizeofFile-song)
                    o.write(data)
                index+=1
                index2+=1

        #Sequences from the DS version (not implemented)
        if fileType == ".dsxm":
            NI = 1
            #Get known values anyways
            unknown = f.read(1)
            totalPatterns = f.read(1)[0]
            patternTableSize = f.read(1)[0]
            f.seek(1, 1)
            tempo = upint(f.read(4))
            #Extra info for documentation purposes
            PatternStart = 0x40
            
        #Presets from the soundactivity minigame (not implemented)
        if fileType == ".sng":
            NI = 1
        
        #Audio from the Wii version (incomplete, has crackling!)
        if fileType == ".wiive":
            #Used later to tell when the next chunk starts
            reads = 0
            C = 1
            print("Rubik's World (Wii) audio")
            channels = upint(f.read(4))
            rate = upint(f.read(4))
            f.read(4)
            f.read(4)
            ileave = upint(f.read(4))*channels
            samples = bupint(f.read(4))
            with open(basepath+f"/{name}.wav", "w+b") as o:
                #Start off by writing the important info to the WAV file
                o.write(strings[0])
                o.write(pint(samples))
                o.write(strings[1])
                o.write(b'\x10\x00\x00\x00\x01\x00')
                o.write(pshort(channels))
                o.write(pint(rate))
                o.write(b'\x10\xB1\x02\x00\x04\x00\x10\x00')
                o.write(strings[2])
                o.write(pint(samples-0x24))
                
                for i in range(samples):
                    if reads >= ileave and C == 1:
                        f.seek(ileave, 1)
                        reads = 0
                        C*=-1
                        offset = f.tell()
                    smpl = pshort(bupshort(f.read(2)))
                    reads+=1
                    o.write(smpl)
                    offset = f.tell()
                    f.seek(ileave, 1)
                    smpl = pshort(bupshort(f.read(2)))
                    reads+=1
                    o.write(smpl)
                    f.seek(offset)
                    if reads >= ileave and C == -1:
                        f.seek(ileave, 1)
                        reads = 0
                        C*=-1
                        offset = f.tell()
        
        #XML file handler
        if fileType == ".xml":
            print("These can be opened with a text editor like Notepad.")
        
        #Sound name list
        if fileType == ".xwb":
            count = upshort(f.read(2))
            for i in range(count):
                unknown = f.read(2)
                soundNameSize = upshort(f.read(2))
                soundName = f.read(soundNameSize).decode("utf-8")
                print(soundName)
        if NI == 1:
            print(f"{fileType} isn't implemented yet, but it is planned.")

#A script for unpacking Plants vs. Zombies data_pack files
#(This is for the DS version!)
#Has a lot of comments in case someone that's new to coding finds this. I hope they're helpful!



import os #Used to create our output folders
from SimpleFileLibrary.all import * #Import the simple file library (just lowers how much typing is needed here. Feel free to use it if you want to.)

#A list of "magic" values that gets checked later. Probably isn't needed, but there really isn't a reason to remove it I guess.
fMagicList = ["RGCN", "RLCN", "RTFN", "RCSN", "RECN", "RNAN", "RCMN", "RAMN", "NARC", "#und"]

magic = "ARCV" #If a file has a header string, put it here for later.
fileType = "data_pack" #Change this to whatever format you're extracting

#Open the files (this creates a list of files for the upcoming loop)
opened_files = open_files()

#Run a loop that goes through every input file
for file in opened_files:
    infoTable = [] #Append everything to this
    
    #Begin by making a variable that stores our path
    basepath = os.getcwd()+f"/Unpacked/{fileType}/"+os.path.splitext(os.path.basename(file))[0]

    #If the path we want to create doesn't exist, make the path. If it already does, this gets skipped.
    if os.path.exists(basepath) != True:
        os.makedirs(basepath)

    #Open the package info file (logs stuff like file offsets, sizes and the unknown values)
    with open(basepath+"_Log.txt", "w+") as L:
        with open(file, "r+b") as f:
            #Using "magic" from earlier, check if this file matches the format this is for
            check = f.read(4).decode("UTF-8")
            
            #Succeeded        
            if check == magic:
                print(f"You opened a valid {fileType} file.")
            
            #Failed
            if check != magic:
                print(f"This isn't a valid {fileType} file...")
                quit()
            
            #How many files are in the package
            fileCount = upint(f.read(4))
            
            #The total size of the package
            packSize = upint(f.read(4))

            #Write the first 2 variables to the log file
            L.write("data_pack "+str(hex(fileCount))+" "+str(hex(packSize))+"\n")
            
            for data in range(fileCount):
                name = str(data)
                while len(name) <=3:
                    name = "0"+name
                fileName = name #The files are nameless, so they'll be numbered.
                fileOffset = upint(f.read(4))
                fileSize = upint(f.read(4))
                unknown = upint(f.read(4)) #I genuinely have no idea what this is for
                info = fileOffset, fileSize, unknown #format the data to be put into the list

                #Write this data as a line into the log file (useful for potentially repacking these)
                L.write(str(hex(fileOffset))+" "+str(hex(fileSize))+" "+str(hex(unknown))+"\n")
                
                #Add the info to the info table
                infoTable.append(info)

            #Begin the file extraction process
            for info in infoTable:
                f.seek(info[0])
                name = str(info[0])#.split("x")[1]
                while len(name) <= 7:
                    name = "0"+name

                try:
                    #Use file "magic" to tell which format is which (and append the extension to the filename)
                    fMagic = f.read(4).decode("UTF-8")
                    if fMagic == "RGCN":
                        name = name+".NCGR"
                    if fMagic == "RLCN":
                        name = name+".NCLR"
                    if fMagic == "RTFN":
                        name = name+".NFTR"
                    if fMagic == "RECN":
                        name = name+".NCER"
                    if fMagic == "RCSN":
                        name = name+".NSCR"
                    if fMagic == "RNAN":
                        name = name+".NANR"
                    if fMagic == "RCMN":
                        name = name+".NMCR"
                    if fMagic == "RAMN":
                        name = name+".NMAR"
                    if fMagic == "NARC":
                        name = name+".NARC"
                    if fMagic == "#und":
                        name = name+".ITX"
                    #If the file type is unknown, just call it .bin
                    if fMagic not in fMagicList:
                        name = name+".BIN"
                    name = str(name).upper()
                except:
                    #UTF-8 decoding error. Just assign .bin to the filename.
                    name = name+".BIN"
                #Seek back by 4 to get the entire file in the next part
                f.seek(-4, 1)
                #Write the output file
                with open(basepath+f"/{name}", "w+b") as o:
                    o.write(f.read(info[1]))

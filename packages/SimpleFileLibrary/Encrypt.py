#String scrambler + "encryption" (can be reversed)
import random
#import struct
#from Numbers import *

#A random name/word generator where the output can be used as a seed.
def randomnamegen():
    p1 = ["So", "Bl", "Br", "Bw", "B", "Bu", "Ma", "Mi", "Ri", "Ro", "Lu"]
    p2 = ["is", "ig", "na", "ni", "ri", "bs", "in", "im", "ir", "i", "en", "em", "er", "un", "um", "om"]
    p3  = ["i", "on", "c", "o", "y", "x", "k", "gus", "gle", "gis", "kus", "kis", "ker", "ks", "kle", "ey", "ie", "er","ld", "ldo"]
    string  = f'{random.choice(p1)}{random.choice(p2)}{random.choice(p3)}'
    return string
#A function that generates a random seed using a list
def generate_seed():
    #The seed generation list (done this way to ensure it's all a string and doesn't contain any non-ascii characters)
    sRand = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "_", " ", "=", "+", "*", "/", 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    #The seed size list. Whichever value gets chosen will be the length of the final seed.
    sizes = [16,32,48,64]
    #Choose a length from the sizes list for the seed
    seedLength = random.choice(sizes)
    files = 0 #Leftover from my old script. Might get used eventually for when support for binary files gets added.
    #Create the seed variable
    seed1 = str(random.choice(sRand))
    #Generate a seed that's at the size of seedLength
    for i in range(seedLength-1):
        seed1 = seed1+str(random.choice(sRand))
    return seed1, seedLength

#A function that encrypts an input file by shifting the bits by a specified amount
def encrypt_file(input_file, output_file, shift_amount):
    #Open the input and output files in binary mode
    read = 0
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        #On the first read, write the amount to the output file
        if read == 0:
            fout.write(pint(shift_amount))
            read = 1
        #Read the input file byte by byte
        byte = fin.read(1)
        while byte:
            #Convert the byte to an integer
            num = int.from_bytes(byte, 'big')
            #Shift the bits by the shift amount
            num = (num << shift_amount) % 256
            #Convert the integer back to a byte
            byte = num.to_bytes(1, 'big')
            #Write the byte to the output file
            fout.write(byte)
            #Read the next byte from the input file
            byte = fin.read(1)

#A function that decrypts an input file by shifting the bits back by a specified amount
def decrypt_file(input_file, output_file, shift_amount):
    # Open the input and output files in binary mode
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        # Read the input file byte by byte
        byte = fin.read(1)
        while byte:
            # Convert the byte to an integer
            num = int.from_bytes(byte, 'big')
            # Shift the bits by the negative shift amount
            num = (num >> shift_amount) % 256
            # Convert the integer back to a byte
            byte = num.to_bytes(1, 'big')
            # Write the byte to the output file
            fout.write(byte)
            # Read the next byte from the input file
            byte = fin.read(1)

#A function that shifts bits by the amount you tell it to
def encrypt(message, shift):
    #Convert the message to binary
    binary = "".join(format(ord(c), "08b") for c in message)
    #Shift the bits by the given amount
    shifted = binary[shift:] + binary[:shift]
    #Convert the shifted binary back to characters
    encrypted = "".join(chr(int(shifted[i:i+8], 2)) for i in range(0, len(shifted), 8))
    #Return the encrypted message
    return encrypted

#A function that shifts bits by the amount you tell it to (in the opposite direction of the previous one)
def decrypt(message, shift):
    #Convert the message to binary
    binary = "".join(format(ord(c), "08b") for c in message)
    #Shift the bits to the right by the given amount
    shifted = binary[-shift:] + binary[:-shift]
    #Convert the shifted binary back to characters
    decrypted = "".join(chr(int(shifted[i:i+8], 2)) for i in range(0, len(shifted), 8))
    #Return the decrypted message
    return decrypted

#Shuffles/scrambles text
def shuffle_text(text):
    #Initialize an empty string and two empty lists
    newstring = ""
    shiftlist = []
    letterlist = []
    #Shuffle the text
    for i in range(len(text)):
        #Make sure no repeated characters get added by checking if what we have is in the shiftlist list
        while True:
            #Choose a random value within the length of the text string
            shift = random.randint(0, len(text)-1)
            #Break the loop if the value is not in the shiftlist list
            if shift not in shiftlist:
                break
        #L = Letter. It grabs a letter using shift as the index.
        L = text[shift]
        #Add the letter to newstring, effectively shuffling the text string
        newstring = newstring+L
        #Now add these to the shiftlist and letterlist lists for later (used to de-scramble the text/data)
        shiftlist.append(shift)
        letterlist.append(L)
    #Return the shuffled string and the two lists
    return newstring, shiftlist, letterlist

#Reverses the shuffling/scrambling done by the previous function
def deshuffle_text(newstring, shiftlist, letterlist):
    #Initialize an empty string and a variable to keep track of the sequence
    restored = ""
    seq = 0
    #De-shuffle the text using the lists we generated
    for i in range(len(newstring)):
        #Find the index of seq in the shiftlist list
        index = shiftlist.index(seq)
        #Get the corresponding letter from the letterlist list
        L = letterlist[index]
        #Add the letter to restored, effectively deshuffling the string
        restored = restored+L
        #Increment the seq variable by 1 to get the next letter in the letter list
        seq+=1
    #Return the restored string
    return restored

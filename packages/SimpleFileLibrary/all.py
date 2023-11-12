#A script that gets every other part of the library and basically combines it into a single module.
#To import everything at once, start your script with "from SimpleFileLibrary.all import*"
from SimpleFileLibrary.Numbers import *
#The BigNumbers module needs to be reworked.
from SimpleFileLibrary.BigNumbers import *
#Structures is still unfinished. Add functions for reversing the creation of stuff and simplify it a bit.
from SimpleFileLibrary.Structures import *
#Maybe FileHandler and FileManagement should be combined into a single script...
from SimpleFileLibrary.FileHandler import *
from SimpleFileLibrary.FileManagement import *
#Maybe ReverseStrings should be combined with Encrypt...
from SimpleFileLibrary.ReverseStrings import *
from SimpleFileLibrary.Encrypt import *
#Functions for handling model data
from SimpleFileLibrary.MeshStuff import *

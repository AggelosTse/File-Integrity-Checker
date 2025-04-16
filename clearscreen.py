import os

def clearscr():
    if os.name == "nt":      
        os.system("cls")  # Windows
    else:
        os.system("clear")  # for Mac and linux
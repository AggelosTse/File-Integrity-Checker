import hashlib
import os
import time

from calculateHash import calculate_file_hash
from clearscreen import clearscr
from verifyHash import verify_file_integrity


def main():
    
    clearscr()
    print("Εργαστηριακή Άσκηση - Έλεγχος Ακεραιότητας Αρχείων\n")
    
    oldHashValue = None     # it contains the hash value when it's created
    hash_created = False    # bool variable checking if the hash value is created or not
    algorithms = ["md5", "sha-1", "sha-256", "sha3-256"]    
    
    while True:
        
        print("1. Create hash value for file \n")       #start the program depending on user's choise
        print("2. Confirm hash value for file \n")
        print("3. Exit program \n")
        
        useranswer = input()
        while useranswer not in ["1", "2", "3"]:        #making sure input is valid
            clearscr()
            useranswer = input("Input wrong, try again. \n")
        
        if useranswer == "1":
            clearscr()
            
            algo = input("What type of algorithm: \n").strip().lower()  
            while algo not in algorithms:                                   #checking for valid user input
                algo = input("Error occurred. Try again with a valid algorithm: (MD5, SHA-1, SHA-256, SHA3-256) \n").strip().lower()
                
                
            clearscr()
            file_path = input("Give file path \n")
            
            current = calculate_file_hash(file_path, algo)          #function that calculates the current hash value
            
            oldHashValue = current                          #when hash value is created, it is stored in this variable
            if current:
                print(f"Hash value of the file: {current}")
                time.sleep(3)  
                clearscr()
                hash_created = True     #hash value created successfully
            else:
                print("Failed to generate hash.\n")     #if anything goes wrong, current will be empty, so it goes back to menu
            
        elif useranswer == "2":
            if not hash_created:                     #you can confirm the hash value ONLY if there's already one created.
                print("Error occured. Hash value not created. \n")
                time.sleep(2)
                clearscr()
                continue 
            
            clearscr()
            algo = input("What type of algorithm: \n").strip().upper() 

            while algo not in algorithms:
                algo = input("Error occurred. Try again with a valid algorithm: (MD5, SHA-1, SHA-256, SHA3-256) \n").strip().upper()

            file_path = input("Give file path \n")        
            original = input(f"Give the original hash value: (latest hash value of the file: {oldHashValue}) \n")
            current = calculate_file_hash(file_path, algo)      #creates a hash value again for the file
            
            if current:
                sameOrNot = verify_file_integrity(original, current)    #then checks if the latest hash value created, is the same as the old one
                if sameOrNot:
                    print("The hash values are the same.")
                else:
                    print("The hash values are different.")
            oldHashValue = None         #at the end of every loop, variables are gettin initialized again, for the next loop.
            hash_created = False
        else:
            print("Exiting program.")
            return
        
        time.sleep(2)
        clearscr()

if __name__ == "__main__":
    main()

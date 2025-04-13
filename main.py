import hashlib
import os
import time

from calculateHash import calculate_file_hash
from verifyHash import verify_file_integrity


def main():
    os.system("clear") 
    print("Εργαστηριακή Άσκηση - Έλεγχος Ακεραιότητας Αρχείων\n")
    
    hash_created = False
    algorithms = ["MD5", "SHA-1", "SHA-256", "SHA3-256"]
    
    while True:
        
        print("1. Create hash value for file \n")       #start the program depending on user's choise
        print("2. Confirm hash value for file \n")
        print("3. Exit program \n")
        
        useranswer = input()
        while useranswer not in ["1", "2", "3"]:        #making sure input is valid
            os.system("clear")
            useranswer = input("Input wrong, try again. \n")
        
        if useranswer == "1":
            os.system("clear")
            
            algo = input("What type of algorithm: \n").strip().upper()  
            while algo not in algorithms:
                algo = input("Error occurred. Try again with a valid algorithm: (MD5, SHA-1, SHA-256, SHA3-256) \n").strip().upper()

            file_path = input("Give file path \n")
            
            current = calculate_file_hash(file_path, algo)          #function that calculates the current hash value
            if current:
                print(f"Hash value of the file: {current}")
                time.sleep(7)  
                os.system("clear") 
                hash_created = True 
            else:
                print("Failed to generate hash.\n")
            
        elif useranswer == "2":
            if not hash_created:                     #you can confirm the hash value ONLY if there's already one created.
                print("Error occured. Hash value not created. \n")
                time.sleep(2)
                os.system("clear")
                continue 
            
            algo = input("What type of algorithm: \n").strip().upper() 

            while algo not in algorithms:
                algo = input("Error occurred. Try again with a valid algorithm: (MD5, SHA-1, SHA-256, SHA3-256) \n").strip().upper()

            file_path = input("Give file path \n")        
            original = input("Give the original hash value: \n")
            current = calculate_file_hash(file_path, algo)      #creates a hash value again for the file
            
            if current:
                sameOrNot = verify_file_integrity(original, current)    #then checks if the latest hash value created, is the same as the old one
                if sameOrNot:
                    print("The hash values are the same.")
                else:
                    print("The hash values are different.")
                
        else:
            print("Exiting program.")
            return
        
        time.sleep(2)
        os.system("clear")

if __name__ == "__main__":
    main()

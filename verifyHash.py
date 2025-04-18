import time
import hmac

def verify_file_integrity(original_hash, current_hash):
    if not original_hash or not current_hash:          #checks if both hash values are valid
        print("Error occured. One or both of the hash values are invalid. \n")
        time.sleep(2)
        return  
    if hmac.compare_digest(original_hash, current_hash):        #using the compare digest function helps on avoiding timing attacks
        print("Hash values are the same. \n")
    else:
        print("Hash values are different. \n")
    time.sleep(2)
    
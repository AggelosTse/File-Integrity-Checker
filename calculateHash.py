import hashlib


def calculate_file_hash(file_path, algorithm):  #takes the path of a file, and the user's algorithm choise
    if algorithm == "md5":          
        hash_obj = hashlib.md5()    #creates a hash object depending on the algorithm. (This object will contain the hash value)
    elif algorithm == "sha-1":
        hash_obj = hashlib.sha1() 
    elif algorithm == "sha-256":
        hash_obj = hashlib.sha256()
    elif algorithm == "sha3-256":
        hash_obj = hashlib.sha3_256() 
    else:
        print("Error occured. Algorithm name is not correct. \n")
        return None
    
    try:
        with open(file_path, 'rb') as f:    #opens it in read binary mode, reads it in raw bytes so it can break it in chunks
            while True:
                block = f.read(4096)  # "break" the file into smaller chuncks of 4096 bytes
                if not block:         # if there's no other block left, it stops
                    break
                hash_obj.update(block)  # Feed block into the hash object
        return hash_obj.hexdigest()     #creates the final hash value and returns it
    except FileNotFoundError:
        print("Error occured. File doesnt exist or couldnt be found. \n")
        return None
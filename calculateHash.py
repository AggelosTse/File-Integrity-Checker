import hashlib


def calculate_file_hash(file_path, algorithm):
    if algorithm == "MD5":
        hash_obj = hashlib.md5()
    elif algorithm == "SHA-1":
        hash_obj = hashlib.sha1()
    elif algorithm == "SHA-256":
        hash_obj = hashlib.sha256()
    elif algorithm == "SHA3-256":
        hash_obj = hashlib.sha3_256()
    else:
        print("Error occured. Algorithm name is not correct. \n")
        return None
    
    try:
        with open(file_path, 'rb') as f:
            for block in iter(lambda: f.read(4096), b''):
                hash_obj.update(block)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"Error occured. File doesnt exist or couldnt be found. \n")
        return None
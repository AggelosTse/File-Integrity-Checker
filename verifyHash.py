def verify_file_integrity(original_hash, current_hash):
    if not original_hash or not current_hash:
        print("Error occured. One or both of the hash values are invalid. \n")
        return False
    return original_hash == current_hash
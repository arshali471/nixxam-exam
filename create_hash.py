import os
import hashlib

files = [f for f in os.listdir('.') if os.path.isfile(f)]


def create_hash():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    for fls in files:
        file = fls  # Location of the file (can be set a different way)
        BLOCK_SIZE = 65536  # The size of each read from the file

        with open(file, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    hash = file_hash.hexdigest()  # Get the hexadecimal digest of the hash
    return hash

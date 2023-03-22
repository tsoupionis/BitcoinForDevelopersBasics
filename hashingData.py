# Importing the hashlib library
import hashlib

# Creating a string and prinnting it out
mystring = 'Python is fun'
print('Your string is:', mystring)

# Hashing the string with SHA256 algorithm and printing it out 
myhash = hashlib.sha256(mystring.encode())
print('Your SHA256 hash is:', myhash.hexdigest())

# No matter what the data is, the hash will always be of length 64
print('The length of your hash is:', len(myhash.hexdigest()))
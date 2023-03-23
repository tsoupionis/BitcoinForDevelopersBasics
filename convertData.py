# Import base58 library
import base58 

#Create string
mystring = b'Hello, world'

#Convert string to base58
mybase58 = base58.b58encode(mystring)

# Prints it out 
print('Base58 String:')
print(mybase58)

#Doing the reverse conversion 
mynumber = 27 
myhexnumber = hex(mynumber)

print('Hex number:')
print(myhexnumber)

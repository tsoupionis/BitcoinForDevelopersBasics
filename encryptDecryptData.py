from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA 
from binascii import hexlify 

message = b'This is a secret message!'

# Before we can encrypt we will need a key pair. so we will generate a private key
private_key = RSA.generate(1024)

#Then we use that private key to derive a public key
public_key = private_key.publickey()

#Print out our keys to be sure we have generated them properly 
#The proper output should be "class 'Crypto.PublicKey.RSA.RSaKey'"
print(type(private_key), type(public_key))

#Convert our keys to strings, save them in .pem files
private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()

#Be sure they are now strings 
print(type(private_pem), type(public_pem))

#Save the strings to .pem files
with open('private.pem', 'w') as pr: 
    pr.write(private_pem)
with open('public.pem', 'w') as pu:
    pu.write(public_pem)

#print the key files out
print('private.pem')
with open('private.pem', 'r') as f:
    print(f.read())
print('public.pem')
with open('public.pem', 'r') as f:
    print(f.read())

#convert the key files back into RSA key objects
pr_key = RSA.import_key(open('private.pem', 'r').read())
pu_key = RSA.import_key(open('public.pem', 'r').read())

#Make sure they are now RSA key objects
print(type(pr_key), type(pu_key))

#Now let's encrypt the message
cipher = PKCS1_OAEP.new(key=pu_key)
cipher_text = cipher.encrypt(message)
print(cipher_text)

#Decrypt the message back to its original form
decrypt = PKCS1_OAEP.new(key=pr_key)
decrypted_message = decrypt.decrypt(cipher_text)

#check if it work 
print(decrypted_message)
#if you get here, it works!
print("Done!")
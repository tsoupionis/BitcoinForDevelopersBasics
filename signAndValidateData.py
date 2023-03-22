# ecdsa library that supporyts secp256k1 (pip install ecdsa)
from ecdsa import SigningKey, SECP256k1

# generate a key specifying SECP256k1 (which curve to use for signing) - Private key
sk = SigningKey.generate(curve=SECP256k1) #type of signature Bitcoin specifically uses
# Add our public, or verifying key
vk = sk.verifying_key

# creating a message, signing it, then printing it 
signature = sk.sign(b"Not your keys, not your coins!")
print(signature)

# Let's check the signature
assert vk.verify(signature, b"Not your keys, not your coins!")

print("If your script runs to this point without an error, congrats, you successfully validated the signature!")

#Why is this so impimportant for Bitcoin? We can be assued that people have the funds they should have:
#THE PERSON WITH THE PRIVATE KEY
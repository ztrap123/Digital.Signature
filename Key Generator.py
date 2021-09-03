from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
keyPair = RSA.generate(2048)
with open('publicKey.out','w') as pubK:
	pubKey = keyPair.publickey()
	print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
	pubKeyPEM = pubKey.exportKey()
	print(pubKeyPEM.decode('ascii'),file=pubK)

with open('privateKey.out','w') as priKey: 
	print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
	privKeyPEM = keyPair.exportKey()
	print(privKeyPEM.decode('ascii'),file = priKey)
 
#encryption
#msg = b'A message for encryption'
#encryptor = PKCS1_OAEP.new(pubKey)
#ncrypted = encryptor.encrypt(msg)
#print("Encrypted:", binascii.hexlify(encrypted))
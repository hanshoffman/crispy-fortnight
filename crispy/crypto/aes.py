import base64
from Crypto.Cipher import AES
from Crypto import Random

class AESCipher:
    def __init__(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
	plaintext = pad(plaintext)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(self.key, AES.MODE_CBC, iv)
	return base64.b64encode(iv + cipher.encrypt(plaintext))
    
    def decrypt(self, ciphertext):
	enc = base64.b64decode(ciphertext)
	iv = en[:16]
	cipher = AES.new(self.key, AES.MODE_CBC, iv)
	return unpad(cipher.decrypt(ciphertext[16:]))

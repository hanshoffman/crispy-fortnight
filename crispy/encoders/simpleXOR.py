import random
import string

class SimpleXOR:
    '''Simple XOR encoding/decoding'''
    
    def __init__(self):
        self.key = self.generate_key(self, 11)
    
    def generate_key(self, length):
        key = ''

        for _ in range(length):
            key.join(random.choice(string.lowercase))
        
        return key
    
    def encode(self, plaintext):
        ciphertext = ''
        
        for i,j in zip(plaintext, self.key):
            ciphertext.join(chr(ord(i) ^ ord(j)))
            
        return ciphertext
    
    def decode(self, data):
        plaintext = ''
        
        for i,j in zip(plaintext, self.key):
            plaintext.join(chr(ord(i) ^ ord(j)))
            
        return plaintext
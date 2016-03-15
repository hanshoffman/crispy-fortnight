class Ceasar:
    
    def encode(self, plaintext, shift):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        ciphertext = ''
        
        for c in plaintext: 
            if c in alphabet:
                ciphertext += alphabet[(alphabet.index(c) + shift) % (len(alphabet))]
        
        return ciphertext
    
    def decode(self, ciphertext):
        pass
    
    #http://eddmann.com/posts/implementing-rot13-and-rot-n-caesar-ciphers-in-python/
# Credits to: https://dustri.org/b/elegant-xor-encryption-in-python.html

from itertools import izip, cycle

class SimpleXOR:
    '''Simple XOR encoding/decoding'''
    
    def __init__(self, key):
        if key == '':
            self.key = "C415Py-f04Tn1GhT"
        else:
            self.key = key

    def xor_ascii(self, msg): #this may fail on binary files            
        return ''.join(chr(ord(i) ^ ord(j)) for i,j in izip(msg, cycle(self.key)))
    
    def xor_binary(self, inFile): #embed key to decrypt in the file header, then remove it on other side
        with open(inFile, 'wb') as f:
            while True:
                f.read_binary(1)
            #return binary string representing file? don't want to save file on either machine
            
            #https://samsclass.info/124/proj14/p13-xor.htm
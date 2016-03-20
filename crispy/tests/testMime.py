import unittest

from crispy.encoders.mime import Mime

class TestMime(unittest.TestCase):
    def test_encrypt(self):
        cipher = Mime()
        self.assertEqual(cipher.encode('crispy'), 'Y3Jpc3B5')
        self.assertEqual(cipher.encode('crispy123!#$% asdfn .. ss'), 'Y3Jpc3B5MTIzISMkJSBhc2RmbiAuLiBzcw==')
    
    def test_decrypt(self):
        cipher = Mime()
        self.assertEqual(cipher.decode('dGhpcyBpcyBhIHRlc3Q='), 'this is a test')
    
if __name__ == '__main__':
    unittest.main()
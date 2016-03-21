import unittest

from crispy.crypto.mime import Mime

class MimeTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cipher = Mime()
        
    def testEncode1(self):
        """Test Encode 1"""
        self.assertEqual(self.cipher.encode('crispy'), 'Y3Jpc3B5')
        
    def testEncode2(self):
        """Test Encode 2"""
        self.assertEqual(self.cipher.encode('crispy123!#$% asdfn .. ss'), 'Y3Jpc3B5MTIzISMkJSBhc2RmbiAuLiBzcw==')

    def testDecode1(self):
        """Test Decode 1"""
        self.assertEqual(self.cipher.decode("dGhpcyBpcyBhIHRlc3Q="), "this is a test")
        
    def testDecode2(self):
        """Test Decode 2"""
        self.assertNotEqual(self.cipher.decode("YWdlbnQ="), "second")
    
if __name__ == '__main__':
    unittest.main()
import unittest

from crispy.encoders.simpleXOR import SimpleXOR

class XORTestCases(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.cipher = SimpleXOR('')
				
	def testEncode1(self):
		"""Test Encode 1"""
		self.assertEqual(self.cipher.xor_ascii('crispy'), ' FXF \x00')
		
# 	def testEncode2(self):
# 		"""Test Encode 2"""
# 		self.assertEqual(self.cipher.xor_ascii("crispy123!#$% asdfn .. ss'), "Y3Jpc3B5MTIzISMkJSBhc2RmbiAuLiBzcw==")
# 		
# 	def testDecode1(self):
# 		"""Test Decode 1"""
# 		self.assertEqual(self.cipher.xor_ascii("dGhpcyBpcyBhIHRlc3Q='), "this is a test")
# 		
# 	def testDecode2(self):
# 		"""Test Decode 1"""
# 		self.assertNotEqual(self.cipher.xor_ascii("HDJFsj23jsjsdf"), "second")

if __name__ == '__main__':
	unittest.main()
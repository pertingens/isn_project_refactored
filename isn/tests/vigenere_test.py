import unittest

from isn import VigenereCipher


class VigenereTest(unittest.TestCase):
    def test_encode(self):
        message = "Hello, world!!!"
        key = "test"

        expected = "Aideh, phvdw!!!"

        self.assertEqual(VigenereCipher.encode(message, key), expected)

    def test_decode(self):
        message = "Aideh, phvdw!!!"
        key = "test"

        expected = "Hello, world!!!"

        self.assertEqual(VigenereCipher.decode(message, key), expected)


if __name__ == "__main__":
    unittest.main()

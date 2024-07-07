# MIT License
# Copyright (c) 2024, Pertingens


import unittest

from isn.cryptography import CaesarCipher


class TestCaesar(unittest.TestCase):
    def test_encode(self):
        message = "Hello, world!"
        expected = "Khoor, zruog!"

        self.assertEqual(CaesarCipher.encode(message, 3), expected)

    def test_decode(self):
        expected = "Hello, world!"
        message = "Khoor, zruog!"

        self.assertEqual(CaesarCipher.decode(message, 3), expected)


if __name__ == "__main__":
    unittest.main()

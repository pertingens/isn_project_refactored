# MIT License
# Copyright (c) 2024, Pertingens


import unittest

from isn import CesarCipher


class TestCesar(unittest.TestCase):
    def test_encode(self):
        message = "Hello, world!"
        expected = "Khoor, zruog!"

        self.assertEqual(CesarCipher.encode(message, 3), expected)

    def test_decode(self):
        expected = "Hello, world!"
        message = "Khoor, zruog!"

        self.assertEqual(CesarCipher.decode(message, 3), expected)


if __name__ == "__main__":
    unittest.main()

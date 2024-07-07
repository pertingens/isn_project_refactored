# MIT License
# Copyright (c) 2024, Pertingens


import os
import cv2
import unittest
import numpy as np

from isn.cryptography import Steganography


class SteganographyTest(unittest.TestCase):
    def test_encode(self):
        message = "this is a test message"
        path_image_to_encode = os.path.join(
            os.path.dirname(__file__), "data", "londres.png"
        )
        path_encoded_image = os.path.join(
            os.path.dirname(__file__), "data", "encoded_image.png"
        )
        image_to_encode = cv2.imread(path_image_to_encode)
        encoded_image = cv2.imread(path_encoded_image)

        encoded_test = Steganography.encode(message, image_to_encode)
        np.testing.assert_array_equal(encoded_test, encoded_image)

    def test_decode(self):
        message = "this is a test message"

        path_encoded_image = os.path.join(
            os.path.dirname(__file__), "data", "encoded_image.png"
        )
        encoded_image = cv2.imread(path_encoded_image)

        decoded_message = Steganography.decode(encoded_image)

        self.assertEqual(decoded_message, message)


if __name__ == "__main__":
    unittest.main()

"""londre_image = cv2.imread("londres.png")
    encoded_image = Steganography.encode_image(
        message="Steganography is a cool technic, hahaha this is a test, blablabla, Lorem ipsum dolor sit amet, consectetur \
              adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
                    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\
                          Excepteur sint occaecat cupidatat non proident, sunt in culpa \
                            qui officia deserunt mollit anim id est laborum",
        image=londre_image,
        chunk_size=3,
    )
    cv2.imwrite("encoded_image.png", encoded_image)

    encoded_image = cv2.imread("encoded_image.png")
    print(Steganography.decode_image(image=encoded_image, chunk_size=3))
    """

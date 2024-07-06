import cv2
import unittest

from isn import Steganography


class SteganographyTest(unittest.TestCase):
    def test_encode(self):
        pass

    def test_decode(self):
        pass


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

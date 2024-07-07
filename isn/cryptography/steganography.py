# MIT License
# Copyright (c) 2024, Pertingens


import numpy as np

from .base_cipher_class import BaseCipherAlgorithm


class Steganography(BaseCipherAlgorithm):
    """Steganography message encoding

    This class implements encoding and decoding based on the
    concept of Steganography. Steganography is a science of
    hiding information inside a medium. This class implements
    Steganography algortihm applied to images. The information is
    hided inside the low-information bits of images.

    More information about Steganography is available at the
    following link: https://en.wikipedia.org/wiki/Steganography

    """

    @staticmethod
    def encode(message: str, image: np.ndarray, chunk_size: int = 4) -> np.ndarray:
        """Encode a message inside an image

        This method encodes a message inside an image using each pixel low-value bits
        as storage capacity.

        Args:
            message (str): The message to encode
            image (np.ndarray): The image to use as transportation medium
            chunk_size (int, optional):
                The number of bits to used for each channel of a pixel,
                The more bit are used, the more detectable the message will be.
                Defaults to 4.

        Raises:
            ValueError:
                If the number of bit is highter than 8 or smaller than 1
            ValueError:
                If the quantity of information is bigger than the possible storage
                capacity of the image.

        Returns:
            np.ndarray: The image containing the message.
        """
        # Check  if parameters are correct
        if chunk_size < 1 or chunk_size > 8:
            raise ValueError(
                f"The number of bit should be included between 1 and 8, not {chunk_size}"
            )

        # Save initial size of the image
        init_size = image.shape

        # Add the end signal
        message = message + "<end>"

        # Create the encoded message
        message = "".join(list(map(lambda x: format(ord(x), "08b"), message)))

        # Split the message in chunks of size {number_bit}
        number_of_chunks = int(np.floor(len(message) / chunk_size))
        chunks = [
            int(message[i : i + chunk_size], 2)
            for i in range(0, number_of_chunks * chunk_size, chunk_size)
        ]

        # Add an uncomplete chunk if necessary, to finish the message
        if len(message) > number_of_chunks * chunk_size:
            last_chunks = message[chunk_size * number_of_chunks :]
            last_chunks = int(last_chunks, 2) * 2 ** (
                len(message) - number_of_chunks * chunk_size - 1
            )
            chunks.append(last_chunks)

        chunks.reverse()
        if len(chunks) > np.prod(image.shape):
            raise ValueError(
                "Impossible to encode the message in the given image, \
                the image is too small, or you need to increase the number of bit used"
            )

        # Encode the message in the image
        image = image.flatten()
        mask_pixel = ~np.uint8(2**chunk_size - 1)

        for i in range(len(image)):
            value_to_encode = chunks.pop()

            new_pixel = (image[i] & mask_pixel) | np.uint8(value_to_encode)
            image[i] = new_pixel

            if len(chunks) == 0:
                break

        image = image.reshape(init_size)

        return image

    @staticmethod
    def decode(image: np.ndarray, chunk_size: int = 4) -> str:
        """Decode an image containing a message

        This method decodes an image containing a message, that was inserted as
        defined in the encode method.

        Args:
            image (np.ndarray): The image containing a message
            chunk_size (int, optional):
                The number of low-value bit used to store the image during the encoding process.
                Defaults to 4.

        Raises:
            ValueError: If the image does not contain any message for the given chunk_size value.

        Returns:
            str: The message contained in the image
        """
        binary_message = []
        mask_pixel = np.uint8(2**chunk_size - 1)
        image = image.flatten()

        for i in range(len(image)):
            value = image[i] & mask_pixel
            binary_message.append(format(value, f"0{chunk_size}b"))

        binary_message = "".join(binary_message)
        message = ""

        for i in range(0, len(binary_message), 8):
            value = binary_message[i : i + 8]
            message += chr(int(value, 2))

        message = message.split("<end>")

        if len(message) < 2:
            raise ValueError("No message found in the image")

        return message[0]

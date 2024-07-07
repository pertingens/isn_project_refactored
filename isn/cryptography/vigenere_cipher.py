# MIT License
# Copyright (c) 2024, Pertingens


import numpy as np

from typing import List

from .caesar_cipher import caesar_encode_chr
from .base_cipher_class import BaseCipherAlgorithm


def _ord_key_char(char: str) -> int:
    """Convert a character to its ASCII representation

    This function convert a character to its ASCII representation. Only
    characters contained in the following regex are converted [a-zA-Z0-9].

    The other are converted to 0.

    Args:
        char (str): The character to be converted

    Returns:
        int: The ASCII representation of the character
    """
    char = ord(char)

    if char >= ord("a") and char <= ord("z"):
        return char - ord("a")

    elif char >= ord("A") and char <= ord("Z"):
        return char - ord("A")

    elif char >= ord("0") and char <= ord("9"):
        return char - ord("0")

    return 0


def _generate_shift_list(
    key: str,
    message: str,
) -> List[int]:
    """Generate the shifting list

    Given a key and a message, this function generates a list of integers
    that represent the shift to apply for each character of the message.

    Args:
        key (str): The key used to generate the shifting list
        message (str): The message to encode

    Returns:
        List[int]: The list of shift values
    """
    shift_list = np.array(list(map(lambda x: _ord_key_char(x), key)))
    shift_list = np.tile(shift_list, int(np.ceil(len(message) / len(shift_list))))[
        : len(message)
    ]

    return shift_list


class VigenereCipher(BaseCipherAlgorithm):
    """Vigenere encryption algortihm

    This class implements encoding and decodig function based on
    the Vigenere algortihm.

    More details on the Vigenere algortihm could be found at
    this link: https://en.wikipedia.org/wiki/Vigenère_cipher

    """

    @staticmethod
    def encode(message: str, key: str) -> str:
        """Vigenere encoding method

        This method takes a message and a key as input, and
        encode the message based on the shift list calculate
        with the key.

        Args:
            message (str): The message to encode
            key (str): The key used to encode the message

        Returns:
            str: The encoded message
        """
        shift_list = _generate_shift_list(key, message)
        message = list(message)

        for i in range(len(message)):
            message[i] = caesar_encode_chr(message[i], shift_list[i])

        return "".join(message)

    @staticmethod
    def decode(message: str, key: str) -> str:
        """Vigenere decode method

        This method take an encoded message and a key as input,
        and decoded the message based on a shift list computed
        with the key.

        Args:
            message (str): The message to decode
            key (str): The key that was used to encode the message

        Returns:
            str: The deocded message
        """
        shift_list = _generate_shift_list(key, message)
        message = list(message)

        for i in range(len(message)):
            message[i] = caesar_encode_chr(message[i], -shift_list[i])

        return "".join(message)

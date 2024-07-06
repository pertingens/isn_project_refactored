# MIT License
# Copyright (c) 2024, Pertingens


import numpy as np

from .caesar_cipher import caesar_encode_chr
from .base_cipher_class import BaseCipherAlgorithm


def _ord_key_letter(letter: str):
    letter = ord(letter)

    if letter >= ord("a") and letter <= ord("z"):
        return letter - ord("a")

    elif letter >= ord("A") and letter <= ord("Z"):
        return letter - ord("A")

    elif letter >= ord("0") and letter <= ord("9"):
        return letter - ord("0")

    return 0


def _generate_shift_list(
    key: str,
    message: str,
):
    shift_list = np.array(list(map(lambda x: _ord_key_letter(x), key)))
    shift_list = np.tile(shift_list, int(np.ceil(len(message) / len(shift_list))))[
        : len(message)
    ]

    return shift_list


class VigenereCipher(BaseCipherAlgorithm):
    @staticmethod
    def encode(message: str, key: str) -> str:
        shift_list = _generate_shift_list(key, message)
        message = list(message)

        for i in range(len(message)):
            message[i] = caesar_encode_chr(message[i], shift_list[i])

        return "".join(message)

    @staticmethod
    def decode(message: str, key: str) -> str:
        shift_list = _generate_shift_list(key, message)
        message = list(message)

        for i in range(len(message)):
            message[i] = caesar_encode_chr(message[i], -shift_list[i])

        return "".join(message)


if __name__ == "__main__":
    message = "hello world, this is a test message, to determine if the vigenere class is working!!!!"
    key = "tes /t, this is a test 9 A key"
    encoded = VigenereCipher.encode(message, key)

    print(encoded)

    print(VigenereCipher.decode(encoded, key))

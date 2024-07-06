# MIT License
# Copyright (c) 2024, Pertingens


from .base_cipher_class import BaseCipherAlgorithm


def caesar_encode_chr(char: str, shift: int) -> str:
    """Encode a character using a shifting mechanism

    This function is used to encode a letter based on a shifting
    mechanism. The letter is first converted to its ASCII representation
    and then shifted by the shift amount.

    Only characters that are included in the following regex will be
    encoded ([a-zA-Z0-9]).

    Args:
        char (str): The letter to encode
        shift (int): The shift used to encode the letter

    Raises:
        ValueError: If the string contains more or less than one character

    Returns:
        str: The encoded letter
    """
    if len(char) > 1 or len(char) < 1:
        raise ValueError(
            f"The character to encode should be exactly of lenght one, not {char}"
        )

    char = ord(char)

    if char >= ord("a") and char <= ord("z"):
        char = ((char - ord("a") + shift) % 26) + ord("a")

    elif char >= ord("A") and char <= ord("Z"):
        char = ((char - ord("A") + shift) % 26) + ord("A")

    elif char >= ord("0") and char <= ord("9"):
        char = ((char - ord("0") + shift) % 10) + ord("0")

    return chr(char)


class CaesarCipher(BaseCipherAlgorithm):
    """Caesar cipher implementation

    This class implements the Cesar cipher cryptographic algorithm. More
    information about the algorithm can be found on wikipedia at the
    following link:

    https://en.wikipedia.org/wiki/Caesar_cipher
    """

    @staticmethod
    def encode(
        message: str,
        shift: int,
    ) -> str:
        """Caesar encode method

        Args:
            message (str): _description_
            shift (int): _description_

        Returns:
            str: _description_
        """
        message = list(map(lambda x: caesar_encode_chr(x, shift), message))
        return "".join(message)

    @staticmethod
    def decode(message: str, shift: int) -> str:
        """Caesar decode method

        Args:
            message (str): _description_
            shift (int): _description_

        Returns:
            str: _description_
        """
        message = list(map(lambda x: caesar_encode_chr(x, -shift), message))
        return "".join(message)

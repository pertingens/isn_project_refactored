def cesar_encode_letter(letter: str, shift: int):
    if len(letter) > 1 or len(letter) < 1:
        raise ValueError(f"letter should be exactly one letter, not {letter}")

    letter = ord(letter)

    if letter >= ord("a") and letter <= ord("z"):
        letter = ((letter - ord("a") + shift) % 26) + ord("a")

    elif letter >= ord("A") and letter <= ord("Z"):
        letter = ((letter - ord("A") + shift) % 26) + ord("A")

    elif letter >= ord("0") and letter <= ord("9"):
        letter = ((letter - ord("0") + shift) % 10) + ord("0")

    return chr(letter)


class CesarCipher:
    @staticmethod
    def encode(
        message: str,
        shift: int,
    ) -> str:
        message = list(map(lambda x: cesar_encode_letter(x, shift), message))
        return "".join(message)

    @staticmethod
    def decode(message: str, shift: int) -> str:
        message = list(map(lambda x: cesar_encode_letter(x, -shift), message))
        return "".join(message)


if __name__ == "__main__":
    encoded = CesarCipher.encode("d hello world 9!!!", 10)

    print(encoded)

    print(CesarCipher.decode(encoded, 10))

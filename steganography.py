import cv2
import numpy as np





def encode_image(
        message: str, 
        image: np.ndarray,
        chunk_size: int = 4
):
    # Check  if parameters are correct
    if chunk_size < 1 or chunk_size > 8:
        raise ValueError(f"The number of bit should be included between 1 and 8, not {chunk_size}")
    
    # Save initial size of the image
    init_size = image.shape

    # Add the end signal
    message = message + "<end>"

    # Create the encoded message
    message = ''.join(list(map(lambda x: format(ord(x), '08b'), message)))

    # Split the message in chunks of size {number_bit}
    number_of_chunks = int(np.floor(len(message) / chunk_size))
    chunks = [int(message[i:i + chunk_size], 2) for i in range(0, number_of_chunks * chunk_size, chunk_size)]

    # Add an uncomplete chunk if necessary, to finish the message
    if len(message) > number_of_chunks * chunk_size:
        last_chunks = message[chunk_size*number_of_chunks:]
        last_chunks = int(last_chunks, 2) * 2**(len(message) - number_of_chunks * chunk_size - 1)
        chunks.append(last_chunks)

    
    chunks.reverse()
    if len(chunks) > np.prod(image.shape):
        raise ValueError(
            f"Impossible to encode the message in the given image, \
            the image is too small, or you need to increase the number of bit used"
        )

    # Encode the message in the image
    image = image.flatten()
    mask_pixel = ~ np.uint8(2 ** chunk_size - 1)

    for i in range(len(image)):
        value_to_encode = chunks.pop()

        new_pixel = (image[i] &  mask_pixel) | np.uint8(value_to_encode)
        image[i] = new_pixel

        if len(chunks) == 0:
            break

    image = image.reshape(init_size)

    return image


def decode_image(
        image: np.ndarray, 
        chunk_size: int = 4
):
    binary_message = []
    mask_pixel = np.uint8(2 ** chunk_size - 1)
    image = image.flatten()

    for i in range(len(image)):
        value = image[i] & mask_pixel
        binary_message.append(format(value, f"0{chunk_size}b"))

    binary_message = "".join(binary_message)
    message = ""

    for i in range(0, len(binary_message), 8):
        value = binary_message[i:i+8]
        message += chr(int(value, 2))
    
    message = message.split('<end>')

    if len(message) < 2:
        raise ValueError("No message found in the image")
    
    return message[0]



    
if __name__ == "__main__":
    londre_image = cv2.imread("londres.png")
    encoded_image = encode_image(
        message="Steganography is a cool technic, hahaha this is a test, blablabla, Lorem ipsum dolor sit amet, consectetur \
              adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
                    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\
                          Excepteur sint occaecat cupidatat non proident, sunt in culpa \
                            qui officia deserunt mollit anim id est laborum",
        image=londre_image,
        chunk_size=3
    )
    cv2.imwrite("encoded_image.png", encoded_image)

    encoded_image = cv2.imread("encoded_image.png")
    print(decode_image(
        image=encoded_image, 
        chunk_size=3
    ))

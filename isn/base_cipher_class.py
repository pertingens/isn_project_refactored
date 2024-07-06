
class BaseCipherAlgorithm:
    """ Abstract base class for Cipher algorithms

    This class should be inherited to define practical
    cipher algorithms.

    It contains an encode and a decode method.

    """
    @staticmethod
    def encode(self, *args, **kwargs):
        """ Encode method

        The encode method takes as input the message to encode
        following the principles of the encoding algorithm, and 
        returns the encoded message in any format following the
        specifications of the encoding algorithm.

        """
        raise NotImplementedError
    
    @staticmethod
    def decode(self, *args, **kwargs):
        """ Decode method

        The decode method takes as input the message to decode and
        returns the decoded message in text format.

        """
        raise NotImplementedError

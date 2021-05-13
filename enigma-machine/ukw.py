class UKW:
    """Code for creating an object for the Rotors"""

    def __init__(self, rotor_name, rotor, dict_letters_pair, etw, rotor_position):

        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.rotor_name = rotor_name
        self.rotor_position = rotor_position
        self.dict_letters_pair = dict_letters_pair

        self.etw = self.ALPHABET
        self.rotor = rotor
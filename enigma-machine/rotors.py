class Rotors:
    """Code for creating an object for the Rotors"""

    def __init__(self, rotor_name, rotor, notch, etw, offset, rotor_position):

        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.rotor_name = rotor_name
        self.offset = offset
        self.rotor_position = rotor_position

        self.etw = self.ALPHABET[self.ALPHABET.index(rotor_position):] + self.ALPHABET[:self.ALPHABET.index(rotor_position)]
        self.rotor = rotor[self.ALPHABET.index(rotor_position):] + rotor[:self.ALPHABET.index(rotor_position)]
        self.notch = notch

    def offset_rotor(self):

        """
        This function reorganizes the rotor wiering based on the offset chosen.

        Without any offset, the Lette "B" would go through the first rotor and come
        out as K, which is a change of 9 index letters. If we change the offset to one,
        the same letter "B" will come out as "F", which is a change of 4 indexes, while 
        that the Letter "C" will com out as "L", which is a change of 9 indexes (Previously was
        the "B" index change). the Whole index changes can be considered as the wiering 
        inside a rotor and changing the offset moves the wires (index).

        For more in-depth explanation and examples on the subject, please visit: 
        https://crypto.stackexchange.com/questions/29315/
        https://pastebin.com/DVip1ypK

        or here:
        http://users.telenet.be/d.rijmenants/en/enigmatech.htm
        """

        temp_list = []
        offset = (27 - self.offset) % 26

        self.rotor = self.rotor[offset:] + self.rotor[:offset]
        for number in range(len(self.rotor)):
            new_letter = self.ALPHABET[self.ALPHABET.find(self.rotor[number])-offset]
            temp_list.append(new_letter)

        self.rotor = "".join(temp_list)

    def rotate_rotor(self):
        """
        Rotates the whole inner core (self.rotor) of the rotor along 
        with its indexes (sefl.etw) once.
        """

        self.etw = self.etw[1:] + self.etw[:1]
        self.rotor = self.rotor[1:] + self.rotor[:1]
from reference_values import *

class RotorEncryption:
    def __init__(self, letter):
        self.letter = letter

    def rotor_ecnryption(self):
        
        """
        This function is resposible for all the rotors encryptions, beginning from the right most ETW (after the plugboar)
        all the way to the reflector and back to the ETW (before the plugboard)
        
        Enigma Machines used to debuggand guide the development of this code.

        Enigma Online: 
        http://people.physik.hu-berlin.de/~palloks/js/enigma/enigma-u_v26_en.html
        https://cryptii.com/pipes/enigma-machine
        """

        # ETW - IN
        output_index = ETW.index(self.letter)

        # ROTORs & ZW - WAY IN
        for rotor in all_rotors[1:]:
            if rotor != ukw:
                input_index = rotor.etw[output_index]
                rotor_encryption = rotor.rotor[output_index]
                output_index = rotor.etw.index(rotor_encryption)
            
            else:
                # UKW
                ukw_enc = ukw.dict_letters_pair.get(ukw.etw[output_index])
                output_index = ukw.etw.find(ukw_enc)


        # ROTORs & ZW - WAY OUT
        for rotor in all_rotors[4::-1]:
            if rotor != ETW:
                input_index = rotor.etw[output_index]
                output_index = rotor.rotor.find(input_index)

                rotor_encryption = zusatzwalze.etw[output_index]

            # ETW - OUT
            else:
                enc_letter = ETW[output_index]

        return enc_letter
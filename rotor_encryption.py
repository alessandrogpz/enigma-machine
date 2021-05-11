#################################################################################################
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
################################################################################################
# IMPORTS

from reference_values import *
################################################################################################

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

        logging.debug(f"\nStart of rotor encryption process for letter '{self.letter}' ------")

        # ETW - IN
        output_index = ETW.index(self.letter)
        logging.debug(f"Index of '{self.letter}' letter in ETW: {str(output_index)}")

        # ROTORs & ZW - WAY IN
        for rotor in all_rotors[1:]:
            if rotor != ukw:
                input_index = rotor.etw[output_index]
                logging.debug(f"\nEntering {rotor.rotor_name} from its right side at: {str(input_index)}")

                rotor_encryption = rotor.rotor[output_index]
                logging.debug(f"Encrypted in {rotor.rotor_name} as: {str(rotor_encryption)}")

                output_index = rotor.etw.index(rotor_encryption)
                logging.debug(f"leaving {rotor.rotor_name} from its left side at index: {str(output_index)}")
            
            else:
                # UKW
                ukw_enc = ukw.dict_letters_pair.get(ukw.etw[output_index])
                logging.debug(f"\nEnters UKW as '{ukw.etw[output_index]}' and gets encrypted as '{ukw_enc}'")

                output_index = ukw.etw.find(ukw_enc)
                logging.debug(f"Leaving UKW at index: {str(output_index)}")

        # ROTORs & ZW - WAY OUT
        for rotor in all_rotors[4::-1]:
            if rotor != ETW:
                input_index = rotor.etw[output_index]
                logging.debug(f"\nEntering {rotor.rotor_name} from its left side at: {str(input_index)}")

                output_index = rotor.rotor.find(input_index)

                rotor_encryption = zusatzwalze.etw[output_index]
                logging.debug(f"Encrypted in {rotor.rotor_name} as: {str(rotor_encryption)}")
                logging.debug(f"leaving {rotor.rotor_name} from its right side at index: {str(output_index)}")

            # ETW - OUT
            else:
                enc_letter = ETW[output_index]

                logging.debug(f"\nEnters ETW at index {output_index} and leaves as letter '{enc_letter}'")
                
                logging.debug("End of rotor encryption process ----------------------")
        return enc_letter
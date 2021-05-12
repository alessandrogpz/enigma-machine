#################################################################################################
import logging
from rotor_encryption import RotorEncryption

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#logging.disable(logging.DEBUG) # When disabled: Show all rotors rotations and double stops 
#logging.disable(logging.INFO)   # When disabled: Show all encryption process

logging.debug('\n----------- Start of main program -----------\n')
#################################################################################################
# IMPORTS

from plugboard import PlugBoard
from rotors_stepping_mechanism import RotorStepMechanism
from reference_values import *
from machine_settings import *
#################################################################################################
# MAIN ENGINE

# Create plugboard connections 
plug_board = PlugBoard.create_plug_board(plugboard_pairs)

# Set all the rotors with their respective offset settings
rotor_1.offset_rotor()
rotor_2.offset_rotor()
rotor_3.offset_rotor()
zusatzwalze.offset_rotor()

for letter in plain_text:
    letter = letter.upper()

    logging.debug("\nStarting encryption process with letter: " + letter)

    if letter.isalpha():

        # PLUGBOARD IN
        letter = PlugBoard(letter, plug_board).check_if_in_plugboard()

        # ROTOR STEPPING MECHANISM
        RotorStepMechanism.rotors_stepping_mechanism()
                      
        # ROTOR ENCRYPTION
        enc_letter = RotorEncryption(letter).rotor_ecnryption()

        # PLUGBOARD OUT
        enc_letter = PlugBoard(enc_letter, plug_board).check_if_in_plugboard()

        enc_text.append(enc_letter)   

    elif letter != " ":
        enc_text.append(letter)

logging.info("\nROTOR FINAL POSITIONS -----------------------")
logging.info("ROTOR 1: " + rotor_1.etw)
logging.info("ROTOR 2: " + rotor_2.etw)
logging.info("ROTOR 3: " + rotor_3.etw)
logging.info("----------------------------------------------")

logging.debug("\nOUTPUT MESSAGE -------------------------------")

# Print the encrypted message
# Insert a space after every 4th element in the enc_list while printing
print("\nEncrypted text: ", end="")

for letter in range(len(enc_text)):
    if count_letter == 3:
        count_letter = 0
        print(enc_text[letter], end=" ")
    else:
        count_letter += 1
        print(enc_text[letter], end="")

logging.debug("\n----------------------------------------------")

logging.debug('\n---------- End of main program -----------\n')


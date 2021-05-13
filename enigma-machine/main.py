from plugboard import PlugBoard
from rotors_stepping_mechanism import RotorStepMechanism
from rotor_encryption import RotorEncryption
from reference_values import *
from machine_settings import *

# Create plugboard connections 
plug_board = PlugBoard.create_plug_board(plugboard_pairs)

# Set all the rotors with their respective offset settings
rotor_1.offset_rotor()
rotor_2.offset_rotor()
rotor_3.offset_rotor()
zusatzwalze.offset_rotor()

for letter in plain_text:
    letter = letter.upper()

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

# Print the encrypted message
# Insert a space after every 4th element in the enc_list while printing
print("\n---------------------------------------------------------------------------------")
print("Ciphertext: ", end="")

for letter in range(len(enc_text)):
    if count_letter == 3:
        count_letter = 0
        print(enc_text[letter], end=" ")
    else:
        count_letter += 1
        print(enc_text[letter], end="")
print("\n---------------------------------------------------------------------------------\n")

# Verbosity output
if args.quiet >= 1:
    pass

elif args.quiet == 0:

    print("Machine End Settings:")
    print(rotor_1.rotor_name + ", Position", rotor_1.etw[0] + ", Offset", str(rotor_1.offset)) 
    print(rotor_2.rotor_name + ", Position", rotor_2.etw[0] + ", Offset", str(rotor_2.offset)) 
    print(rotor_3.rotor_name + ", Position", rotor_3.etw[0] + ", Offset", str(rotor_3.offset)) 

    print(zusatzwalze.rotor_name + ", Position", zusatzwalze.etw[0] + ", Offset", str(zusatzwalze.offset)) 
    print(ukw.rotor_name)

    print("Plugboard", plugboard_choices,"\n")
else:
    pass


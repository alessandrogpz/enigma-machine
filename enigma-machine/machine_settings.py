##################################################################################################
# IMPORTS

from argparse_file import *
###################################################################################################
# MACHINE SETTINGS & PLAIN TEXT 

rotor_chosen = [args.rotor_1, args.rotor_2, args.rotor_3]
rotor_offset = [args.rotor_1_offset, args.rotor_2_offset, args.rotor_3_offset]
rotor_positions = [args.rotor_1_position, args.rotor_2_position, args.rotor_3_position]


zusatzwalze_chosen = [args.zusatzwalze]
zusatzwalze_offset = [args.zusatzwalze_offset]
zusatzwalze_position = [args.zusatzwalze_position]

ukw_chosen = [args.ukw]

# Plugboard input example = ["AB", "CD", "EF"]
plugboard_pairs = plugboard_choices

plain_text = 'This is Enigma'

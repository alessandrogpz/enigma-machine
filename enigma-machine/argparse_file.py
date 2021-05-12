#################################################################################################
# IMPORTS

import argparse
##################################################################################################
# CLI

msg = "This an Enigma Machine simulator"

rotor_choices = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
rotor_positions = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
zusatzwalze_choices = ["ZW-B", "ZW-G"]
ukw_choices = ["UKW-B-THIN","UKW-C-THIN"]
plugboard_choices = []
plain_text_chosen = ""

parser = argparse.ArgumentParser(description = msg)

#Rotor 1
parser.add_argument("rotor_1", help="Assign the first rotor", choices = rotor_choices)
parser.add_argument("rotor_1_position", help="Set an initial position for the first rotor chosen", choices = rotor_positions)
parser.add_argument("rotor_1_offset", help="Set an initial offset for the rotor chosen", choices=range(1,27), type=int)

#Rotor 2
parser.add_argument("rotor_2", help="Assign the second rotor", choices = rotor_choices)
parser.add_argument("rotor_2_position", help="Set an initial position for the second rotor chosen", choices = rotor_positions)
parser.add_argument("rotor_2_offset", help="Set an initial offset for the rotor chosen", choices=range(1,27), type=int)

#Rotor 3
parser.add_argument("rotor_3", help="Assign the third rotor", choices = rotor_choices)
parser.add_argument("rotor_3_position", help="Set an initial position for the third rotor chosen", choices = rotor_positions)
parser.add_argument("rotor_3_offset", help="Set an initial offset for the rotor chosen", choices=range(1,27), type=int)

# Zusatzwalze
parser.add_argument("zusatzwalze", help="Assign the zusatzwalze", choices = zusatzwalze_choices)
parser.add_argument("zusatzwalze_position", help="Set an initial position for the zusatzwalze chosen", choices = rotor_positions)
parser.add_argument("zusatzwalze_offset", help="Set an initial offset for the zusatzwalze chosen", choices=range(1,27), type=int)

parser.add_argument("ukw", help="Assign the UKW", choices = ukw_choices)

# Plugboard
number_of_pair = input("Number of Plugboar letter pairs: ")

if number_of_pair != "":
    for pair in range(int(number_of_pair)):
        pair_chosen = input(f"Pair number {pair+1}: ")
        plugboard_choices.append(pair_chosen.upper())
    else:
        pass

plain_text_chosen = input("Plaintext: ")

parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)

args = parser.parse_args()

if args.verbosity >= 2:

    print("\nMachine Settings")
    print("Rotor:", args.rotor_1 + ", Position:", args.rotor_1_position + ", Offset:", str(args.rotor_1_offset)) 
    print("Rotor:", args.rotor_2 + ", Position:", args.rotor_2_position + ", Offset:", str(args.rotor_2_offset)) 
    print("Rotor:", args.rotor_3 + ", Position:", args.rotor_3_position + ", Offset:", str(args.rotor_3_offset)) 

    print("Zusatzwalze:", args.zusatzwalze + ", Position:", args.zusatzwalze_position + ", Offset:", args.zusatzwalze_offset) 

    print("Reflector:", args.ukw)

    print("Plugboard:", plugboard_choices)

elif args.verbosity == 1:

    print(args.rotor_1, args.rotor_1_position, args.rotor_1_offset) 
    print(args.rotor_2, args.rotor_2_position, args.rotor_2_offset) 
    print(args.rotor_3, args.rotor_3_position, args.rotor_3_offset) 

    print(args.zusatzwalze, args.zusatzwalze_position, args.zusatzwalze_offset) 

    print(args.ukw)

    print(plugboard_choices)
else:
    pass

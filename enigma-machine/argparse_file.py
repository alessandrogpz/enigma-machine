import argparse

msg = """This is an Enigma Machine simulator based on the M4 'Shark' (U-Boats) machines. 
         The arguments needed to initialze the machine are in order for each rotor [Rotor] [Rotor Position] [Rotor Offset] and least of all the Reflector [Reflector].
         An example of a valid argument would be: I A 1 II B 2 III C 3 ZW-B D 4 UKW-B-THIN. 
         Afterwards you will be prompted to insert the of letter pairs used at the plugboard.
         The last step will be to type the text to be ciphered"""

rotor_choices = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
rotor_positions = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
zusatzwalze_choices = ["ZW-B", "ZW-G"]
ukw_choices = ["UKW-B-THIN","UKW-C-THIN"]
pair_letter_choices = []
plugboard_choices = []
plain_text_chosen = ""

parser = argparse.ArgumentParser(description = msg)

#Rotor 1
parser.add_argument("rotor_1", help="Assign the 1st rotor", choices = rotor_choices)
parser.add_argument("rotor_1_position", help="Initial position for 1st rotor", choices = rotor_positions)
parser.add_argument("rotor_1_offset", help="Initial offset for 1st rotor", choices=range(1,27), type=int)

#Rotor 2
parser.add_argument("rotor_2", help="Assign the 2nd rotor", choices = rotor_choices)
parser.add_argument("rotor_2_position", help="Initial position for 2nd rotor", choices = rotor_positions)
parser.add_argument("rotor_2_offset", help="Initial offset for 2nd rotor", choices=range(1,27), type=int)

#Rotor 3
parser.add_argument("rotor_3", help="Assign the 3rd rotor", choices = rotor_choices)
parser.add_argument("rotor_3_position", help="Initial position for 3rd rotor", choices = rotor_positions)
parser.add_argument("rotor_3_offset", help="Initial offset for 3rd rotor", choices=range(1,27), type=int)

# Zusatzwalze
parser.add_argument("zusatzwalze", help="Assign the zusatzwalze", choices = zusatzwalze_choices)
parser.add_argument("zusatzwalze_position", help="Initial position for zusatzwalze", choices = rotor_positions)
parser.add_argument("zusatzwalze_offset", help="Initial offset for zusatzwalze", choices=range(1,27), type=int)

# UKW
parser.add_argument("ukw", help="Assign the Reflector (UKW)", choices = ukw_choices)

# Verbosity argument
parser.add_argument("-q", "--quiet", help="decrease output verbosity", action="count", default=0)

# Initialize arguments
args = parser.parse_args()

# Plugboard
while True:
    number_of_pair = input("Number of Plugboard letter pairs: ")
    if (number_of_pair.isnumeric() and int(number_of_pair) <= 13) or number_of_pair == "":
        break
    else:
        print("Invalid choice. Plugboard letter pairs must be a number in between 0 and 13")


if number_of_pair != "":
    for number in range(int(number_of_pair)):
        while True:
            pair_chosen = input(f"Pair number {number+1}: ").upper()
            
            # Makes sure that all plugboard inputs are finite and uniques.
            # Stores the pair of letters chosen in pair_letter_choices like ["A","B","C","D"]
            if len(pair_chosen)==2 and pair_chosen.isalpha() and pair_chosen[0] != pair_chosen[1] and pair_chosen[0] not in pair_letter_choices and pair_chosen[1] not in pair_letter_choices: 
                pair_letter_choices.append(pair_chosen[0])
                pair_letter_choices.append(pair_chosen[1])
                break
            else:
                print("Invalid choice. Make sure to insert 2 letters at a time and not repeat any letter already inserted")
    
    # Joins every 2 letters in pair_letter_choices in plugboard_choices like ["AB","CD"]
    for letter in range (0, len(pair_letter_choices), 2):
        plugboard_choices.append(pair_letter_choices[letter] + pair_letter_choices[letter+1])
else:
    pass

# Plaintext
plain_text_chosen = input("Plaintext: ")

# Verbosity output
if args.quiet >= 1:
    pass

elif args.quiet == 0:

    print("\nMachine Start Settings:")
    print("Rotor", args.rotor_1 + ", Position", args.rotor_1_position + ", Offset", str(args.rotor_1_offset)) 
    print("Rotor", args.rotor_2 + ", Position", args.rotor_2_position + ", Offset", str(args.rotor_2_offset)) 
    print("Rotor", args.rotor_3 + ", Position", args.rotor_3_position + ", Offset", str(args.rotor_3_offset)) 

    print("Zusatzwalze", args.zusatzwalze + ", Position", args.zusatzwalze_position + ", Offset", args.zusatzwalze_offset) 

    print("Reflector", args.ukw)

    print("Plugboard", plugboard_choices)
else:
    pass

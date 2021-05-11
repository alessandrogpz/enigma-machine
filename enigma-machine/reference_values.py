####################################################################################################
# IMPORTS

from rotors import Rotors
from zw import Zusatzwalze
from ukw import UKW
from machine_settings import *
###################################################################################################
# REFERENCE VALUES

ETW     = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ROTOR_1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
ROTOR_2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE' 
ROTOR_3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO' 
ROTOR_4 = 'ESOVPZJAYQUIRHXLNFTGKDCMWB' 
ROTOR_5 = 'VZBRGITYUPSDNHLXAWMJQOFECK' 
ROTOR_6 = 'JPGVOUMFYQBENHZRDKASXLICTW' 
ROTOR_7 = 'NZJHGRCXMYSWBOUFAIVLPEKQDT' 
ROTOR_8 = 'FKQHTLXOCBJSPDZRAMEWNIUYGV' 

ROTOR_1_NOTCH = 'Q'
ROTOR_2_NOTCH = 'E' 
ROTOR_3_NOTCH = 'V'
ROTOR_4_NOTCH = 'J'
ROTOR_5_NOTCH = 'Z'
ROTOR_6_NOTCH = 'ZM'
ROTOR_7_NOTCH = 'ZM'
ROTOR_8_NOTCH = 'ZM'

ZW_B = 'LEYJVCNIXWPBQMDRTAKZGFUHOS' 
ZW_G = 'FSOKANUERHMBTIYCWLQPZXVGJD'

UKW_B_THIN = 'ENKQAUYWJICOPBLMDXZVFTHRGS'
UKW_C_THIN = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'

UKW_B_THIN_DICT = {'A': 'E', 'B': 'N', 'C': 'K', 'D': 'Q', 'E': 'A', 'F': 'U', 'G': 'Y', 'H': 'W', 'I': 'J', 'J': 'I', 'K': 'C', 'L': 'O', 'M': 'P', 'N': 'B', 'O': 'L', 'P': 'M', 'Q': 'D', 'R': 'X', 'S': 'Z', 'T': 'V', 'U': 'F', 'V': 'T', 'W': 'H', 'X': 'R', 'Y': 'G', 'Z': 'S'}
UKW_C_THIN_DICT = {'A': 'R', 'B': 'D', 'C': 'O', 'D': 'B', 'E': 'J', 'F': 'N', 'G': 'T', 'H': 'K', 'I': 'V', 'J': 'E', 'K': 'H', 'L': 'M', 'M': 'L', 'N': 'F', 'O': 'C', 'P': 'W', 'Q': 'Z', 'R': 'A', 'S': 'X', 'T': 'G', 'U': 'Y', 'V': 'I', 'W': 'P', 'X': 'S', 'Y': 'U', 'Z': 'Q'}

enc_text = [] # Stores all encrypted letters so they can be joined at the end of the encryption process
####################################################################################################
# All ROTORS, ZW & UKW AVAILABLE

all_rotors_dict = {"I":ROTOR_1,
              "II":ROTOR_2, 
              "III":ROTOR_3, 
              "IV":ROTOR_4, 
              "V":ROTOR_5, 
              "VI":ROTOR_6, 
              "VII":ROTOR_7, 
              "VIII":ROTOR_8}

all_notches_dict = {"I":ROTOR_1_NOTCH,
               "II":ROTOR_2_NOTCH,
               "III":ROTOR_3_NOTCH,
               "IV":ROTOR_4_NOTCH,
               "V":ROTOR_5_NOTCH,
               "VI":ROTOR_6_NOTCH,
               "VII":ROTOR_7_NOTCH,
               "VIII":ROTOR_8_NOTCH,}

all_zusatzwalze_dict = {"ZW-B":ZW_B, 
                   "ZW-G":ZW_G}

all_ukw_dict = {"UKW-B-THIN":UKW_B_THIN, 
           "UKW-C-THIN":UKW_C_THIN}

all_ukw_dicts = {"UKW-B-THIN":UKW_B_THIN_DICT, 
                "UKW-C-THIN":UKW_C_THIN_DICT}
###################################################################################################
# ASSIGN CHOSEN SETTINGS TO ROTORS, ZW & UKW

rotor_1 = Rotors(f"Rotor {rotor_chosen[0]}" ,all_rotors_dict.get(rotor_chosen[0]),
                 all_notches_dict.get(rotor_chosen[0]),
                 ETW,
                 rotor_offset[0],
                 rotor_positions[0])

rotor_2 = Rotors(f"Rotor {rotor_chosen[1]}",
                 all_rotors_dict.get(rotor_chosen[1]),
                 all_notches_dict.get(rotor_chosen[1]),
                 ETW,
                 rotor_offset[1],
                 rotor_positions[1])

rotor_3 = Rotors(f"Rotor {rotor_chosen[2]}",
                 all_rotors_dict.get(rotor_chosen[2]),
                 all_notches_dict.get(rotor_chosen[2]),
                 ETW,
                 rotor_offset[2],
                 rotor_positions[2])

zusatzwalze = Zusatzwalze(f"Zusaltzwalze {zusatzwalze_chosen[0]}",
                          all_zusatzwalze_dict.get(zusatzwalze_chosen[0]),
                          ETW, 
                          zusatzwalze_offset[0], 
                          zusatzwalze_position[0])

ukw = UKW(all_ukw_dict.get(ukw_chosen[0]), 
          all_ukw_dicts.get(ukw_chosen[0]), 
          ETW, 
          zusatzwalze_position[0])

all_rotors = [ETW, rotor_1, rotor_2, rotor_3, zusatzwalze, ukw]


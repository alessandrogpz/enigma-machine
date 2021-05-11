#################################################################################################
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
################################################################################################
# IMPORTS

from reference_values import *
from machine_settings import *
##################################################################################################

class RotorStepMechanism:
    def __init__(self):
        pass

    def rotors_stepping_mechanism():
        """
        This method is responsible for the rotor rotations while the machine is working.

        Check if the notch is in rotor_x.etw[-1], if it is, rotate the following rotor with it.
        It also checks for double stops in rotor 2.

        More information about rotor rotation can be found here:
        http://users.telenet.be/d.rijmenants/en/enigmatech.htm
        """
        
        rotor_1.rotate_rotor()

        # Rotate rotor 2
        if (rotor_1.etw[-1] in rotor_1.notch):
            rotor_2.rotate_rotor() 

            logging.info("------------------------------------------")
            logging.info("ROTOR 2 :" + rotor_2.etw)
            logging.info("------------------------------------------")

        # Rotate rotor 2  & 3 - Double Stop
        if (rotor_1.etw[-2] in rotor_1.notch) and (rotor_2.etw[0] in rotor_2.notch):
            rotor_2.rotate_rotor()
            rotor_3.rotate_rotor()

            logging.info("------------------------------------------")
            logging.info("DOUBLE STOP")
            logging.info("ROTOR 2 :" + rotor_2.etw)
            logging.info("ROTOR 3 :" + rotor_3.etw)
            logging.info("------------------------------------------")
        
        # Rotate rotor 3
        if (rotor_1.etw[-1] in rotor_1.notch) and (rotor_2.etw[-1] in rotor_2.notch):
            rotor_3.rotate_rotor()

            logging.info("-------------------------------------------")
            logging.info("ROTOR 3 :" + rotor_3.etw)
            logging.info("-------------------------------------------")
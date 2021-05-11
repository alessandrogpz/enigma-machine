#################################################################################################
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
################################################################################################

class PlugBoard:
    def __init__(self, letter, plugboard):
        self.letter = letter
        self.plugboard = plugboard

    def create_plug_board(list_connections):

        """
        Create a plugboard based on the users input in machine settings plugboard_pairs.
        Returns dict with all connections. 
        """

        logging.debug("\nSTART OF PLUGBOARD DEBUGGER ---------------\n")

        plug_board = {}

        for pair in list_connections:
            plug_board[pair[0]] = pair[1]
            plug_board[pair[1]] = pair[0]

        logging.debug("Plugboard: " + str(plug_board))
        logging.debug("\nEND OF PLUGBOARD DEBUGGER -----------------\n")

        return plug_board

    def check_if_in_plugboard(self):
        """
        Check if letter is in dictionary and return it with its pair if it is.
        Returns itself if not.
        """

        if self.letter in self.plugboard:
            letter = self.plugboard.get(self.letter)
            logging.debug(f"\nLetter: '{self.plugboard.get(letter)}' Swaped by letter '{letter}' during plugboard passthrough.")

            return letter
        else:
            return self.letter

        
                

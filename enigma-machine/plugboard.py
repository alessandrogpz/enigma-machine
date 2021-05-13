class PlugBoard:
    def __init__(self, letter, plugboard):
        self.letter = letter
        self.plugboard = plugboard

    def create_plug_board(list_connections):

        """
        Create a plugboard based on the users input in machine settings plugboard_pairs.
        Returns dict with all connections. 
        """

        plug_board = {}

        for pair in list_connections:
            plug_board[pair[0]] = pair[1]
            plug_board[pair[1]] = pair[0]

        return plug_board

    def check_if_in_plugboard(self):
        """
        Check if letter is in dictionary and return it with its pair if it is.
        Returns itself if not.
        """

        if self.letter in self.plugboard:
            letter = self.plugboard.get(self.letter)

            return letter
        else:
            return self.letter

        
                

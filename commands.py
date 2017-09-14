"""Module for the commands for ChessBot"""

import openings

class Commands():
    """Commands for ChessBot"""
    def __init__(self):
        self.openings = openings.Openings("eco/eco.json")
        self.commands = {"opening": self.opening}

    def execute(self, cmd):
        """Executes a command from chat."""
        split = cmd.split(" ", 1)
        name = split[0]
        args = split[1]
        if name in self.commands:
            return self.commands[name](args)
        else:
            return None

    def opening(self, args):
        """`opening` command"""
        found = self.openings.closest_match(args)
        return "**{0} {1}**. Moves: `{2}`. Board: <https://lichess.org/analysis/{3}>"\
            .format(found.eco, found.name, found.as_pgn_moves(), found.fen.replace(" ", "_"))

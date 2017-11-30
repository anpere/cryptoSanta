from copy import deepcopy
from random import shuffle

from Crypto.PublicKey import RSA
from Crypto import Random

# Edit here to add players
# map from name to handle (email, messenger id, phone number, etc) can be empty
players = {"alice": "alice@aperlas.com",
            "bob": "bob@aperlas.com",
            "charlie": "charlie@aperlas.com"}

class Player(object):
    def __init__(self, name, handle):
        self.name = name
        self.handle = handle
        self.secret_key = ""
        self.public_key = ""
    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.name,
            self.handle,
            self.secret_key,
            self.public_key,
        )
    def assign_player(self, otherPlayer):
        if otherPlayer == self:
            raise ValueError("can't assign player to themself!")
        self.assignment = otherPlayer

class SSAssignment(object):
    """"
    A secret santa assignment, with the following invariants:
        no player is assigned to themself
        every player has one assignment
    """
    def __init__(self, players):
        self.players = [Player(name, handle) for name, handle in players.items()]

    def __str__(self):
        toString = ""
        for player in self.players:
            toString += (str(player) + "\n")
        return toString
    def assign_players(self):
        # Skulls and Crossbones
        # may infinite loop!
        targets = deepcopy(self.players)
        shuffle(targets)
        for player in self.players:
            if player != targets[0]:
                player.assign_player(targets[0])
                targets.pop(0)
            else:
                if len(targets) == 1:
                    self.assignPlayers()
                else:
                    player.assign_player(targets[1])
                    targets.pop(1)
    def get_assignment(self):
        return {player: player.assignment for player in self.players}

    def generate_keys(self):
        for player in self.players:
            rng = Random.new().read
            key = RSA.generate(1024, rng)
            player.secret_key = key.exportKey("PEM")
            player.public_key = key.exportKey("OpenSSH")

    def checkRep():
        raise NotImplemented()

def setupGame():
    game = SSAssignment(players)
    game.assign_players()
    print(game)
    game.generate_keys()
    return game

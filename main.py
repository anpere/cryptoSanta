from players import (
    setupGame
)
from messenger import Emailer
if __name__ == '__main__':
    sender = Emailer()
    game = setupGame()
    player_assignment = game.get_assignment()
    s_msg = "Congrats on playing Secret Santa Your assignment is {}, you may use"\
          "the following secret key to decrypt gift suggestions for them: \n"\
          "{}\n happy playing!"

    public_keys = {player.name: player.public_key for player in game.players}
    p_msg = "Here are the following player public key pairings {}".format(public_keys)
    for player in set(player_assignment):
        print(player)
        ## TODO
        assignment = player.assignment
        msg = s_msg.format(assignment.name, assignment.secret_key)
        sender.send(player.handle, msg)

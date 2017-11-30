from players import (
    setupGame,
    Player,
)
from messenger import Emailer
if __name__ == '__main__':
    sender = Emailer()
    game = setupGame()
    player_assignment = game.get_assignment()
    s_msg = (
        "Player {} has {}. "
        "You may give them the following secret key\n {}\n"
        "Please make public assignment {}'s public key:\n {}\n"
    )

    public_keys = {player.name: player.public_key for player in game.players}
    p_msg = "Here are every player's public keys {}".format(public_keys)
    secret_keys = {player.name: player.secret_key for player in game.players}
    for player in set(player_assignment):
        assignment = player.assignment
        assert isinstance(assignment, Player)
        msg = s_msg.format(
            player.name,
            assignment.name,
            secret_keys[assignment.name],
            assignment.name,
            public_keys[assignment.name],
        )
        sender.send(player.handle, msg)

    print(p_msg)

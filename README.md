# Crypto Santa

## Scenario

You and your friends are playing Secret Santa. You know what your friend Alice wants, but you don't know that Bob has her. You could ask around who has Alice, and Bob may tell you he has her. Bob, however, doesn't know what Alice wants. He wants to ask people for advice, but he doesn't trust anybody to keep his assignment a secret

## Crypto to the Rescue
At the initialization of the game, Bob his given Alice as an assignment, but he is also given a secret key corresponding to Alice.
Alice's public key is known to everybody playing the game. So if anybody has a gift suggestion, they can use Alice's public key to encrypt the message, and only Bob will be able to decrypt it. Bob now knows what to get Alice, and Alice has no idea what the suggestion was.

## How to run:
python main.py
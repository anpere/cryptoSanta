# Crypto Santa

## Scenario

You and your friends are playing Secret Santa. You know what your friend Alice wants, but you don't know that Bob has her. You could ask around who has Alice, and Bob may tell you he has her. Bob, however, doesn't know what Alice wants. He wants to ask people for advice, but he doesn't trust anybody to keep his assignment a secret

## Crypto to the Rescue
At the initialization of the game, Bob is given Alice as an assignment, but he is also given a secret key corresponding to Alice.
Alice's public key is known to everybody playing the game. So if anybody has a gift suggestion, they can use Alice's public key to encrypt the message, and only Bob will be able to decrypt it. Bob now knows what to get Alice, and Alice has no idea what the suggestion was.

## How to run:
This repo is very bare bones and just deals with generating assignments and public key.
At the moment you'd need to print these out on a piece of paper and hand them out.
To add players edit the players variable in players.py
Once you do that, just run:
`python main.py`

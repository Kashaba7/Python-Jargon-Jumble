# Python Jargon Jumble

A small command-line word game about the jargon of software development. Unscramble each word using the sentence clue, then see how many you can get right.

## Requirements

- Python 3

The game uses only Python's standard library; no packages need to be installed.

## Run the game

Clone or download this repository, open a terminal in the project folder, and run:

```bash
python Jargon-Jumble.py
```

On some systems, use `python3` instead:

```bash
python3 Jargon-Jumble.py
```

## How to play

- Unscramble the displayed letters and type your guess.
- Type `hint` to see a clue. You can request it more than once.
- Type `skip` to reveal the answer and move to the next word.
- Type `quit` to end the game.

There are 10 rounds, and each word is selected at most once per game. Your score and a closing message are shown at the end.

## Words and clues

The game includes software and workplace terms such as `standup`, `syntax`, `debug`, `deploy`, and `prototype`. Their clues are defined in the `word_bank` in [Jargon-Jumble.py](./Jargon-Jumble.py).

import random


word_bank = [
    ("standup", "Every morning, our fifteen-minute _ _ _ _ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a _ _ _ _ error."),
    ("debug", "I spent four hours trying to _ _ _ _ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to _ _ _ _ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the _ _ _ _."),
    ("meeting", "That ninety-minute _ _ _ _ could have been an email."),
    ("deadline", "Of course will hit the _ _ _ _, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a _ _ _ _ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the _ _ _ _ is down again."),
    ("prototype", "It's just an early _ _ _ _, so please ignore that clicking anywhere crashes it.")
]

ROUNDS = 10
round_num = 1
used = []
score = 0


while round_num <= ROUNDS:


    word, hint = random.choice(word_bank)
    while (word, hint) in used:
        word, hint = random.choice(word_bank)
    used.append((word, hint))

    

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).upper()
    
    print()
    print(f"\nRound {round_num}")
    print()
    print(f"Scrambled: {scrambled_word}")
    print()

    prompt = "Guess the word, type 'hint' for a clue, 'skip' to skip, or 'quit' to exit. \n"
    guess = input(prompt).strip().lower()

    while guess == "hint":
        print(f"Hint: {hint}")
        guess = input(prompt).strip().lower()

    if guess == "quit":
        print("GOOD BYE!")
        break

    if guess == "skip":
        print(f"Skipped: the word was '{word}'.")
    elif guess == word:
        score += 1
        print("✅ Correct")
    else:
        print(f"❌ Sorry, the word was '{word}'.")

    round_num += 1   


print("Thanks for playing!")
print(f"Final score: {score}/{ROUNDS}")

if score == ROUNDS:
    print("Flawless! All tests passing zero bugs.")
elif score == ROUNDS - 1:
    print("Near perfect, only one failing test!")
elif score == 3:
    print("Good effort! The code runs, and that's what counts.")
else:
    print("Have you tried turning it off and on again?")

import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    missing_index = random.randint(1, length - 2)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    return progression, correct_answer


def play_progression_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for i in range(3):
        progression, correct_answer = generate_progression()
        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;"
                  "(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()

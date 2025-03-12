import math
import random


def lcm(a, b, c):
    """Функция для вычисления наименьшего общего кратного трех чисел."""
    return math.lcm(a, math.lcm(b, c))


def play_lcm_game():
    """Логика игры по нахождению НОК."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):  # Три раунда игры
        numbers = [random.randint(1, 100) for _ in range(3)]  # Генерация 3 случайных чисел
        correct_answer = lcm(*numbers)  # Вычисление НОК
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_lcm_game()

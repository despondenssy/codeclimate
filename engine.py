import prompt

ROUNDS_COUNT = 3  # Количество раундов

def run_game(game):
    """
    Универсальный движок для игр.
    
    :param game: модуль игры, который должен содержать:
                 - game.TASK (описание игры)
                 - game.generate_round() -> (вопрос, правильный ответ)
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.TASK)

    for i in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
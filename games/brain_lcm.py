import random
import math

TASK = "Find the smallest common multiple of given numbers."

def generate_round():
    """Генерирует вопрос и правильный ответ для игры 'НОК'."""
    numbers = [random.randint(1, 20) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = math.lcm(*numbers)  # Вычисляем НОК
    return question, correct_answer
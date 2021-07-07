import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def guess_number(number):
    '''Берем половину из диапазона, сравниваем с загаданным числом.
    Сравниваем полученное число с загаданным и
    задаем новый диапазон, который будем рассматривать.
    Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    last_number = 100
    first_number = 1
    predict = last_number // 2

    while number != predict: # выход из цикла, если угадали
        count += 1 # увеличиваем число попыток
        if number > predict:
            first_number = predict + 1 # меняем начало диапазона для поиска загаданного числа
        elif number < predict:
            last_number = predict - 1 # меняем конец диапазона для поиска загаданного числа
        predict = (last_number+first_number) // 2 # берем средину от диапазона, где находиться загаданное число

    return (count)


print("УГАДАЙ ЧИСЛО!")
print("Компьютер загадывает целое число от 1 до 100.")
print("Затем угадывает.")
print("Алгоритм будет запущен 1000 раз и выведено среднее количество попыток угадать число.")
# запускаем угадывание чисел
score_game(guess_number)

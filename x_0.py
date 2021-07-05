import random

matrix = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]


def print_matrix():
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()


def check_winning_combinations(computer_step):
    if matrix[1][1]=="-":
        matrix[1][1] = computer_step
    else:
        while True:
            i = random.randint(0,2)
            j = random.randint(0,2)
            if matrix[i][j]=="-":
                matrix[i][j] = computer_step
                break


def entering_move(user_first, is_first):
    computer_step = int(not user_first)
    if user_first:
        if is_first:
            while True:
                #step_user = list(map(int, (input("Введите свой ход: ").split(" "))))
                # проверка ввода
                step_user = input("Введите свой ход: ").split(" ")
                if len(step_user)!=2:
                    print("Введите две координаты!")
                    continue
                i = step_user[0]
                j = step_user[1]
                if not(i.isdigit()) or not(j.isdigit()):
                    print("Нужно вводить цифры!")
                    continue
                i, j = int(i), int(j)
                if not(0<=i<=2) or not(0<=j<=2):
                    print("Введите значение от 0 до 2!")
                    continue
                if matrix[i][j]!="-":
                    print("Данное поле уже занято, введите другой ход!")
                else:
                    break
            matrix[i][j] = int(user_first)
        else:
            check_winning_combinations(computer_step)
    else:
        if is_first:
            check_winning_combinations(computer_step)
        else:
            while True:
                step_user = list(map(int, (input("Введите свой ход: ").split(" "))))
                i = step_user[0]
                j = step_user[1]
                if matrix[i][j] != "-":
                    print("Данное поле уже занято, введите другой ход!")
                else:
                    break
            matrix[i][j] = int(user_first)


def check_result_game(user_step):
    computer_step = not user_step
    is_draw = True
    for i in range(3):
        for j in range(3):
            if matrix[i][j]=="-":
                is_draw = False
    if is_draw:
        return "Ничья."
    elif (matrix[0][0]==user_step and matrix[0][1]==user_step and matrix[0][2]==user_step
    or matrix[1][0]==user_step and matrix[1][1]==user_step and matrix[1][2]==user_step
    or matrix[2][0]==user_step and matrix[2][1]==user_step and matrix[2][2]==user_step
    or matrix[0][0]==user_step and matrix[1][0]==user_step and matrix[2][0]==user_step
    or matrix[0][1]==user_step and matrix[1][1]==user_step and matrix[2][1]==user_step
    or matrix[0][2]==user_step and matrix[1][2]==user_step and matrix[2][2]==user_step
    or matrix[0][0]==user_step and matrix[1][1]==user_step and matrix[2][2]==user_step
    or matrix[0][2]==user_step and matrix[1][1]==user_step and matrix[2][0]==user_step):
        return "Вы выиграли! Поздравляем!"
    elif (matrix[0][0]==computer_step and matrix[0][1]==computer_step and matrix[0][2]==computer_step
    or matrix[1][0]==computer_step and matrix[1][1]==computer_step and matrix[1][2]==computer_step
    or matrix[2][0]==computer_step and matrix[2][1]==computer_step and matrix[2][2]==computer_step
    or matrix[0][0]==computer_step and matrix[1][0]==computer_step and matrix[2][0]==computer_step
    or matrix[0][1]==computer_step and matrix[1][1]==computer_step and matrix[2][1]==computer_step
    or matrix[0][2]==computer_step and matrix[1][2]==computer_step and matrix[2][2]==computer_step
    or matrix[0][0]==computer_step and matrix[1][1]==computer_step and matrix[2][2]==computer_step
    or matrix[0][2]==computer_step and matrix[1][1]==computer_step and matrix[2][0]==computer_step):
        return "Вы проиграли."
    else:
        return ""


print_matrix()
who_first = int(input("Кто ходит первым? 1 - Вы, 0 - компьютер "))
user_first = int(who_first == 1)
print("Формат ввода - x y")
print("x - номер строки, от 0 до 2")
print("y - номер столбца, от 0 до 2")
while True:
    entering_move(user_first, True)
    result = check_result_game(user_first)
    print_matrix()
    if result:
        print(result)
        break
    entering_move(user_first, False)

print_matrix()


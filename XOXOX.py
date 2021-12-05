def intro(): #Отрисовка поля
    print("%%%%%%%%%%%%%%%%%%%")
    print("      Игра в       ")
    print("  крестики-нолики  ")
    print("%%%%%%%%%%%%%%%%%%%")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print("%%%%%%%%%%%%%%%%%%%")

def enter():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def check(): #Обработка ошибок пользователя
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def winner(): #Варианты алгоритмов поиска победителя
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Нолик!!!")
            return True
    return False


intro()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    enter()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = check()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if winner():
        break

    if count == 9:
        print(" Ничья!")
        break

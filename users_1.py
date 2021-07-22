name_1=input('Игрок 1 - Введите ваше имя:')
name_2=input('Игрок 2 - Введите ваше имя:')
print(f'Добрый день, {name_1} и {name_2}')
print(f'Первым ходит {name_1}')

def choose():
    while True:
       choise=input(f'{name_1}, выберите, за кого хотите начать Х или О?:').split()
       if (choise[0].lower() == 'х' or choise[0].lower() == 'x') and len(choise) == 1:
           return True
       elif (choise[0].lower() == 'о' or choise[0].lower() =='o') and len(choise) == 1:
           return False
       else:
            print("Введите, пожалуйста, только Х или О")
            continue

def field_build():
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))

def move(f):
    while True:
        step = input('Выберите координаты для хода:').split()
        if len(step) != 2:
            print("Введите, пожалуйста, только две координаты через пробел")
            continue
        if not (step[0].isdigit() and step[1].isdigit()):
            print("Введите, пожалуйста, только числа")
            continue
        x, y = map(int, step)
        if not(0<=x<3 and 0<=y<=2):
            print('Введите координаты, незаходящие за рамки поля игры')
            continue
        if f[x][y] in "-":
           return x, y
        else:
            print('Клетка уже занята, введите, пожалуйста другие координаты, чтобы продолжить игру')

def win(f,user1,user2):
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    L = [*f[0], *f[1], *f[2]]
    for c in positions:
        symbols=[]
        for c1 in c:
            symbols.append(L[c1])
            if symbols==['x','x','x']:
                print(f'Победа {user1}')
                return True
            if symbols==['о','о','о']:
                print(f'Победа {user2}')
                return True
    return False

field = []
for i in range(3):
    field.append(['-'] * 3)

count=0

if choose():
    while True:
        count += 1
        field_build()
        if count % 2 == 1:
            print(f"Ходит {name_1}!")
        else:
            print(f"Ходит {name_2}!")
        x, y = move(field)
        if count % 2 == 1:
            field[x][y] = 'x'
        else:
            field[x][y] = 'о'
        if win(field,name_1,name_2):
            break
        if count == 9:
            print('Ничья!')
            break
else:
    while True:
        count += 1
        field_build()
        if count % 2 == 1:
            print(f"Ходит {name_1}!")
        else:
            print(f" Ходит {name_2}!")
        x, y = move(field)
        if count % 2 == 1:
            field[x][y] = 'о'
        else:
            field[x][y] = 'x'
        if win(field,name_2,name_1):
            break
        if count == 9:
            print('Ничья!')
            break
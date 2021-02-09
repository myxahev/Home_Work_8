import random



class LotoCard:
    """Генерация игровой карточки"""

    def __init__(self, name_player):
        self.name_player = name_player

    def gen_card(self):
        self.card = [i for i in range(1, 91)]
        random.shuffle(self.card)
        self.card = self.card[:15]
        return self.card

    def __str__(self):
        line1 = sorted(self.card[:5])
        line2 = sorted(self.card[5:10])
        line3 = sorted(self.card[10:15])

        num_i = [i for i in range(1, 5)]
        j = 0

        while len(line1) < 9 and len(line2) < 9 and len(line3) < 9:
            random.shuffle(num_i)
            line1.insert(num_i[0 + j], "  ")
            random.shuffle(num_i)
            line2.insert(num_i[0 + j], "  ")
            random.shuffle(num_i)
            line3.insert(num_i[0 + j], "  ")
            j += 1
        line1 = ' '.join(map(str, line1))
        line2 = ' '.join(map(str, line2))
        line3 = ' '.join(map(str, line3))

        return f'{str(self.name_player).center(27, "-")}\n{line1}\n{line2}\n{line3}\n{"-" * 27}'


class LotoGame:
    """Механизм игры"""

    def gen_bag(self):
        self.bag = [i for i in range(1, 91)]
        random.shuffle(self.bag)
        #print(self.bag)
        self.one_barrel = self.bag[0]
        return self.one_barrel

player_1 = LotoCard('Евгений')
pl1 = player_1.gen_card()
#print(player_1)

ai_player = LotoCard('Компьютер')
ai = ai_player.gen_card()
#print(ai_player)

game = LotoGame()
ga = game.gen_bag()
#print(ga)
"""
for i in pl1:                                     # проходимся в цикле по значению боченка по списку карточки игрока
    print(player_1)                               # вывод карточек и номера боченка
    print(ai_player)
    print(ga)
    if isinstance(pl1, int):
        if input('Зачеркнуть цифру? (y/n) ') == 'y':  # если пользователь ответил вычеркнуть
            if i == ga:                               # проверка соответстви боченка на значении в карточке игрока
                pl1[i] = ' - '                        # заменяем значение ячейки на прочерк в карточке игрока
                for ii in ai:                         # проходимся в цикле по значению боченка по списку карточки компьтера
                    if isinstance(ai, int):
                        if ii == ga:                  # проверка соответстви боченка на значении в карточке компьтера
                            ai[ii] = ' - '            # заменяем значение ячейки на прочерк в карточке компьютера
                    else:
                        print('Выиграл компьютер')
                #continue                              # продолжаем играть
            else:
                print('Вы проиграли')                 # если нет значение "Вы проиграли"
                break

        if input('Зачеркнуть цифру? (y/n) ') == 'n':  # если пользователь ответил нет
            if i != ga:                               # проверка на не соответстви боченка на значении в карточке игрока
                continue                              # продолжаем играть
            else:
                print('Вы проиграли')                 # если есть значение "Вы проиграли"
                break
    else:
        print('Вы выиграли')
"""


for i in range(91):
    print(player_1)
    print(ai_player)
    print('Номер выпавщего боченка: ', ga)
    # Ход игрока
    if isinstance(pl1, int):
        if input('Зачеркнуть цифру? (y/n) ') == 'y':
            if pl1.index(ga) != ga[0]:                #косяк: нужна проверка значения ga на значение из списка pl1
                print('You lose')
                break
            pl1[pl1.index(ga)] = '-'
        if input('Зачеркнуть цифру? (y/n) ') == 'n':
            if i == ga:
                print('You lose')
                break
    else:
        print('You win')
        break
    # Ход компьютера
    if isinstance(ai, int):
        if ai.index(ga) == ga[0]:                    #косяк: нужна проверка значения ga на значение из списка ai
            ai[ai.index(ga)] = '-'
    else:
        print('You lose, PC win')
        break
    ga.pop(0)

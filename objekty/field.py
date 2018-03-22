from objekty.box import Box
import errorz

class Field:

    def __init__(self):
        self.field = []
        for _ in range(81):
            box = Box()
            self.field.append(box)

    def nacti_vstup(self, vstup):
        upraveny_vstup = ''
        with open(vstup, encoding='utf-8') as opened_file:
            for line in opened_file:
                upraveny_vstup += ''.join(str(line).strip().split(' '))
            if len(upraveny_vstup) != 81:
                raise errorz.InputError(upraveny_vstup, 'v zadani chybi/prebyvaji policka')
        i = 0
        for j in upraveny_vstup:
            if j in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                self.field[i].zapis_hodnotu(int(j))
            i += 1


    def vytiskni(self):
        for i in range(9):
            for j in range(9):
                val = (self.field[i * 9 + j]).value
                if val:
                    print(val, end='')
                else:
                    print('x', end='')
                if (j+1)%3 == 0:
                    print(' ', end='')
            print()
        print()


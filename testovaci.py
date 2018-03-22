from objekty import field
from objekty import area
import parametry
import metody

if __name__ == '__main__':
    hraci_pole, not_solved_areas = metody.inicializace()
    hraci_pole.vytiskni()
    for i in range(9):
        print(hraci_pole.field[i].possible_values)

    BOX = hraci_pole.field[1]

    arey = metody.areas_with_box(BOX, not_solved_areas)

    for oblast in arey:
        oblast.aplikuj_condition1(BOX.value)

    for i in range(9):
        print(hraci_pole.field[i].possible_values)

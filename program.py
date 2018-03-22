import metody


if __name__ == '__main__':
    hraci_pole, not_solved_areas = metody.inicializace()
    hraci_pole.vytiskni()

    for policko in hraci_pole.field:
        if policko.value:
           arey = metody.areas_with_box(policko, not_solved_areas)
           for oblast in arey:
               oblast.aplikuj_condition1(policko.value)

    for i in hraci_pole.field:
        if not i.value and len(i.possible_values) == 1:
            i.zapis_hodnotu(i.possible_values[0])



    hraci_pole.vytiskni()
    for i in range(9):
        print(hraci_pole.field[i].value)




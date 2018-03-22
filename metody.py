import parametry
from objekty import field
from objekty import area
from objekty import box


def inicializace():
    hraci_pole = field.Field()
    hraci_pole.nacti_vstup('zadani')
    seznam_oblasti = parametry.radky + parametry.sloupce + parametry.ctverce
    not_solved_areas = []
    for indexy in seznam_oblasti:
        new_area = area.Area(hraci_pole, indexy)
        not_solved_areas.append(new_area)
    return hraci_pole, not_solved_areas


def areas_with_box(policko, seznam_oblasti):
    ty_oblasti = []
    for oblast in seznam_oblasti:
        if policko in oblast.field:
            ty_oblasti.append(oblast)
    return(ty_oblasti)
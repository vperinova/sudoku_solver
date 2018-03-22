import errorz

class Area:

    def __init__(self, pole, list_of_indexes):
        self.field = []
        for i in list_of_indexes:
            self.field.append(pole.field[i])

    def solved(self):
        for b in self.field:
           if not b.value:
               return False
        return True

    def condition1(self, number):
        '''pokud je v nejakem boxu hodnota n, nebude uz v zadnem jinem'''
        count = 0
        for b in self.field:
            if b.value == number:
                count += 1
        if count > 1:
            raise errorz.SolutionError0('stejna hodnota ve vice polich')
        if count == 1:
            return 1
        return 0

    def condition2(self, number):
        '''pokud lze cislo napsat jen do jednoho boxu, vrati ten box'''
        count = 0
        the_box = 0
        for b in self.field:
            if number in b.possible_values:
                count += 1
                the_box = b
        if count == 0:
            raise errorz.SolutionError(number, 0, 'condition2 - neni kam zapsat')
        if count == 1:
            return the_box
        else:
            return 0

    def aplikuj_condition1(self, number):
        if self.condition1(number):
            for b in self.field:
                b.odeber_poss_value(number)
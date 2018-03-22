import errorz

class Box:

    def __init__(self):
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = 0

    def zapis_hodnotu(self, k):
        if self.value and self.value != k:
            raise errorz.SolutionError0('Nemuzeme zapisovat do plneho boxu')
        self.possible_values = [k]
        self.value = k

    def odeber_poss_value(self, n):
        if n in self.possible_values and not self.value:
            self.possible_values.remove(n)
            moznych = len(self.possible_values)
            if moznych == 0:
                raise errorz.SolutionError0('Oops, je tu box, do ktereho nemuzeme nic napsat')



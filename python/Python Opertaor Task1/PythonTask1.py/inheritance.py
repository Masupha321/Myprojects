class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class div_mod(division, modulus):
    def __init__(self, a, b):
        division.__init__(self, a, b)
        modulus.__init__(self, a, b)

    def div_and_mod(self):
        divval = self.divide()             
        modval = self.mod_divide()
        return divval, modval



x = div_mod(10, 3)
print("division:", x.divide())
print("mod_division:", x.mod_divide())
print("divmod:", x.div_and_mod())

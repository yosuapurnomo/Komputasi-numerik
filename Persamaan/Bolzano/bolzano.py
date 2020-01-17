# import decimal as Dec

class bolzano:
    def __init__(self):
        self.x1 = float(input("X1 = "))
        self.x2 = float(input("X2 = "))
        self.n = lambda x: ((x ** 3) + (4 * (x ** 2))) - 10
        # self.n = lambda x: ((x ** 3) + (x ** 2) - 3 * x) - 3
        self.coun = 0
        self.temp = 0

    def proses(self):
        self.Fx1 = round(self.n(self.x1), 3)
        self.Fx2 = round(self.n(self.x2), 3)
        self.x3 = round((self.x1 + self.x2) / 2, 3)
        self.Fx3 = round(self.n(self.x3), 3)
        if self.Fx3 == self.temp:
            print(f"Hasil Akhir = {self.x3}")
            return 0
        self.coun += 1
        print(f"""Interasi ke {self.coun}
Fx1 = {self.Fx1}      Fx2 = {self.Fx2}      X3 = {self.x3}     Fx3 = {self.Fx3}""")

        if self.Fx3 == 0:
            print(f"Hasil Akhir = {self.x3}")
        elif (self.Fx3 * self.Fx1) < 0:
            self.temp = self.Fx3
            self.x2 = self.x3
            self.proses()
        elif (self.Fx3 * self.Fx2) < 0:
            self.temp = self.Fx3
            self.x1 = self.x3
            self.proses()


start = bolzano()
start.proses()

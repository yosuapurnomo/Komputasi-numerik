import decimal as Dec

class regula:
    def __init__(self):
        self.x1 = float(input("X1 = "))
        self.x2 = float(input("X2 = "))
        self.n = lambda x: (x ** 3 + x ** 2) - (3 * x) - 3
        # self.rumus_x3 = lambda x1, x2, fx1, fx2: (x1 * fx2) - (x2 * fx1) / (fx2 - fx1)
        self.coun = 0

    def proses(self):
        self.Fx1 = round(self.n(self.x1), 2)
        self.Fx2 = round(self.n(self.x2), 2)
        self.x3 = round((self.x1 * self.Fx2) - (self.x2 * self.Fx2) / (self.Fx2 - self.Fx1), 2)
        self.Fx3 = round(self.n(self.x3), 2)
        self.coun += 1
        print(f"""Interasi ke {self.coun}
Fx1 = {self.Fx1}    Fx2 = {self.Fx2}    X3 = {self.x3}      Fx3 = {self.Fx3}""")
        if self.Fx3 == 0.0:
            print(f"Hasil Akhir = {self.x3}")
        elif (self.Fx3 * self.Fx1) < 0:
            self.x2 = round(self.x3, 2)
            self.proses()
        elif (self.Fx3 * self.Fx2) < 0:
            self.x1 = round(self.x3, 2)
            self.proses()


start = regula()
start.proses()

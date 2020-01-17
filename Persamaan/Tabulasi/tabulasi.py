class tabulasi:
    def __init__(self):
        self.n = lambda x: round(2 * x - 5, 2)
        # self.n = lambda x: round(x**3 - 2 * x + 5, 2)
        self.a = 5
        self.coun = float(1)
        self.interasi = 0
        self.temp2 = 0

    def counter(self):
        self.interasi += 1
        print(f"Interasi ke {self.interasi}")
        print("A = ", self.a)
        print(f"Hasil F(a) = {self.n(self.a)}\n")
        if self.n(self.a) == self.temp2:
            print(f"X = {round(self.a, 2)} = {abs(round(self.n(self.a), 2))}")
        elif self.n(self.a) == 0.0:
            print(f"X = {round(self.a, 2)} = {abs(round(self.n(self.a), 2))}")
        elif self.n(self.a) > 0:
            self.temp = round(self.a, 2)
            # print(f"Temp = {self.temp}")
            self.temp2 = self.n(self.a)
            self.a = round(self.a - self.coun, 2)
            # print(f"A = {self.a}")
            self.counter()
        elif self.n(self.a) < 0:
            # print("A < 0 = ", self.n(self.a))
            self.coun = self.coun / 10
            self.temp2 = self.n(self.a)
            self.a = round(self.temp, 2)
            self.counter()


start = tabulasi()
start.counter()

import numpy
import matplotlib.pyplot as plot

class Regnesi_linier:
    def __init__(self):
        self.X = []
        self.y = []
        self.sumY = float()
        self.sumX = float()
        self.sumX2 = float()
        self.sumX3 = float()
        self.sumXY = float()

    def setXY(self):
        self.X.append(float(input(f"Input X ke {(len(self.X) + 1)} =  ")))
        self.y.append(float(input(f"Input Y ke {len(self.y) + 1} = ")))
        if input("ulang = ") is "y":
            self.setXY()

    def setValue(self):
        self.sumY = numpy.sum(self.y)
        self.sumX = numpy.sum(self.X)
        self.sumX2 = numpy.sum((numpy.array(self.X) ** 2))
        self.sumX3 = numpy.sum(self.X) ** 2
        self.sumXY = numpy.sum((numpy.array(self.X) * numpy.array(self.y)))

        print(f"""X = {self.X}      Y = {self.y}
Sum X = {self.sumX}     Sum(X^2) = {self.sumX2}     Sum(X)^2 = {self.sumX3}
Sum Y = {self.sumY}     Sum( X*Y) = {self.sumXY}""")

    def Hasil(self):
        self.n = float(input("Nilai x yang diCari = "))

        self.C = round(
            ((self.sumY * self.sumX2) - (self.sumX * self.sumXY)) / (((len(self.X)) * self.sumX2) - self.sumX3), 2)
        print("Nilai C = ", self.C)

        self.M = round(
            ((len(self.X)) * self.sumXY - self.sumX * self.sumY) / (((len(self.X)) * self.sumX2) - self.sumX3), 2)
        print("Nilai M = ", self.M)

        self.hasil = (self.M * self.n) + self.C
        print("Hasil Akhir = ", self.hasil)


    def inter_Polasi(self):
        print("INTER POLASI")
        self.cariX = float(input("Inter Polasi X yang diCari = "))
        for i in range(len(self.X)):
            if self.X[i] < self.cariX < self.X[i + 1]:
                self.hasilY = self.y[i] + ((self.y[i + 1] - self.y[i]) / (self.X[i + 1] - self.X[i])) * (
                        self.cariX - self.X[i])
                print(f"Hasil Inter Polasi {self.cariX} = ", self.hasilY)
                self.X.append(self.cariX)
                self.y.append(self.hasilY)
                plt = plot
                plt.scatter(self.X, self.y)
                plt.show()
                break
            elif self.cariX in self.X:
                print(f"Hasil Inter Polasi {self.cariX} = ", self.y[self.X.index(self.cariX)])
                break


start = Regnesi_linier()
start.setXY()
start.setValue()
start.Hasil()
start.inter_Polasi()

import numpy

class integal:
    def __init__(self):
        self.bawah = float(input("X 1 = "))
        self.atas = float(input("X 2 = "))
        self.h = float(input("H = "))
        temp = round(self.atas - self.bawah, 1)
        self.r = int(round(temp/self.h, 1))
        self.xIndex = [self.bawah]
        self.exponen = 2.7182818285
        self.xr = []
        self.hasil = []

    # def setR(self):
    #     print("R = ", self.r)

    def setX(self):
        for i in range(0, self.r):
            self.bawah +=self.h
            self.xIndex.append(round(self.bawah, 1))
        print(self.xIndex)
        self.setXR()
        self.hasilAkhir()

    def setXR(self):
        for i in range(0, len(self.xIndex)):
            self.xr.append(round((self.exponen**self.xIndex[i]), 2))
        print(self.xr)

    def hasilAkhir(self):
        for i in range(0, len(self.xr)):
            if i is 0 or i is (len(self.xr)-1):
                self.hasil.append(self.xr[i])
                # print()
            else:
                self.hasil.append((2*self.xr[i]))
        print(self.hasil)
        hasilAkhir = numpy.array(self.hasil)
        print(round(self.h/2*(numpy.sum(hasilAkhir)), 2))


run = integal()
run.setX()

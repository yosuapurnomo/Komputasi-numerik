import numpy


class error:
    def __init__(self):
        self.awal = []
        self.prediksi = []
        self.error_selisi = []
        self.error_relatif = []
        self.jumlah_error = None

    def setError(self):
        text = "Nilai ke %(kode)s", (len(self.awal) + 1, " = ")
        self.awal.append(float(input(text)))
        self.prediksi.append(float(input(text)))
        tes = input("Ulang = ")
        if tes is "y":
            return self.setError()
        print(self.awal)
        self.setError_prediksi()
        self.setError_relativ()
        self.Mad()
        self.Made()

    def setError_prediksi(self):
        print("Error Prediksi")
        for i in range(0, len(self.awal)):
            self.error_selisi.append(abs(self.awal[i]-self.prediksi[i]))
        print(self.error_selisi)

    def setError_relativ(self):
        print("Error Relativ")
        for i in range(0, len(self.awal)):
            self.error_relatif.append(round(((self.error_selisi[i]/self.awal[i])*100), 1))
        print(self.error_relatif)
        # self.jumlah_error = numpy.array(self.error_relatif)
        hasil = numpy.sum(self.error_relatif)
        print(hasil / len(self.awal))
    def Mad(self):
        self.mad = numpy.sum(self.error_selisi) * (1/len(self.awal))
        print(f"Hasil Mad = {self.mad}")
    def Made(self):
        self.made = numpy.sum(self.error_relatif) * (1/len(self.awal))
        print(f"Hasil Made = {self.made}")


start = error()
start.setError()

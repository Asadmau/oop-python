class PersegiPanjang():
    # function yang di panggil pertama kali
    def __init__(self, p , l):
        self.p = p
        self.l = l
    def info(self):
        return f'Modul OOP Menggunakan Python studi persegi ! panjang {self.p} ' \
               f'lebar {self.l}'
    def hitung(self):
        return self.p * self.l / 2
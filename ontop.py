class Libro:
    def __init__(self, titolo, anno, autore):
        self.titolo = titolo
        self.anno = anno
        self.autore = autore

    def get_titolo(self):
        return self.titolo

    def get_anno(self):
        return self.anno

    def get_autore(self):
        return self.autore

    def set_titolo(self, titolo):
        self.titolo = titolo

    def set_anno(self, anno):
        self.anno = anno

    def set_autore(self, autore):
        self.autore = autore

    def __str__(self):
        return f"{self.titolo}, {self.anno}, {self.autore}"


if __name__ == "__main__":
    libro = Libro("Il nome della rosa", 1980, "Umberto Eco")
    print(libro)



from Arucikk import Arucikk

class GumiKalapacs(Arucikk):
    def __init__(self, ar, tomeg, fej_meret):
        super().__init__(ar, tomeg)
        self.fej_meret = fej_meret
        self._nev = "Gumi kalapács"

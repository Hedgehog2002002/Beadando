from Fizetes import Fizetes
import re

class KartyasFizetes(Fizetes):
    def __init__(self, osszeg, kartyaszam, lejarati_datum):
        super().__init__(osszeg)
        self._kartyaszam = kartyaszam
        self._lejarati_datum = lejarati_datum

    def fizet(self, penz):
        return self.letezo_kartya() and penz > self.osszeg

    def letezo_kartya(self):
        return re.match('([0-9]{4}-){3}[0-9]{4}', self._kartyaszam) is not None

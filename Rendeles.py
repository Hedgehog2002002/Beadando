from datetime import date

class Rendeles:
    def __init__(self, arucikkek):
        self._datum = date.today()  # mai nap lekérése a Python datetime moduljából
        self._reszletek = ''
        self.arucikkek = arucikkek

    def osszegez(self):
        return sum([arucikk.ar + arucikk.szallitasi_koltseg for arucikk in self.arucikkek])

    def osszegez_adoval(self):
        return self.osszegez() * 1.2

    def kifizet(self, vevo, kartyaszam = None, lejarati_datum = None):
        if kartyaszam is None or lejarati_datum is None:
            self._reszletek += f'{vevo.nev} készpénzzel kíván fizetni.\n'
            fizetes = Keszpenz(osszeg)

        else:
            self._reszletek += f'{vevo.nev} kártyával ({kartyaszam, lejarati_datum}) kíván fizetni.\n'
            fizetes = KartyasFizetes(osszeg, kartyaszam, lejarati_datum)

        siker = fizetes.fizet(vevo.penz)

        if siker:
            self._reszletek += f'Sikeres fizetés!\n'
            self._reszletek += f'A megvásárolt árucikkek: {", ".join([arucikk.__str__() for arucikk in self.arucikkek])}\n'
            vevo.penz -= osszeg
        else:
            self._reszletek += f'Sikertelen fizetés! :(\n'

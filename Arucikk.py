class Arucikk:
    def __init__(self, ar, tomeg):
        self.ar = ar
        self._tomeg = tomeg
        self._szallitasi_koltseg = self.szallitast_szamol(tomeg)
        self._nev = ""

    @property
    def szallitasi_koltseg(self):
        return self._szallitasi_koltseg

    @property
    def tomeg(self):
        return self._tomeg

    @tomeg.setter
    def tomeg(self, ertek):
        self._tomeg = ertek
        self._szallitasi_koltseg = self.szallitast_szamol(ertek)


    def szallitast_szamol(self, tomeg):
        return tomeg + (tomeg / 100)

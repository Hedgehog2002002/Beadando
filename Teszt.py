from Arucikk.GumiKalapacs import GumiKalapacs
from Arucikk.Lezerkard import Lezerkard
from Rendeles import Rendeles
from Vevo import Vevo

ani = Vevo("Anakin Skywalker", "Tatooine 12", 250)
obi_wan = Vevo("Obi-Wan Kanobi", "Stewjon 4", 350)

rendeles1 = Rendeles([GumiKalapacs(25, 5, 50), Lezerkard(100, "zöld")])
rendeles2 = Rendeles([Lezerkard(120, "kék")])

rendeles1.kifizet(ani)
rendeles2.kifizet(obi_wan, "5133-3367-8912-3456", "02/22")

print(rendeles1)
print(rendeles2)

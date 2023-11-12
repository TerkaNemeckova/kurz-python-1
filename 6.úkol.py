class Auto:
    def __init__(self, registracni_znamka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znamka = registracni_znamka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne == True:
            print("Potvrzuji zapůjčení vozidla.")
            self.dostupne = False
        else:
            print("Vozidlo není k dispozici.")

    def get_info(self):
        return self.registracni_znamka + " " + self.typ_vozidla

    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.najete_km = stav_tachometru
        self.dostupne = True
        if pocet_dni < 7:
            cena = pocet_dni * 400
        elif pocet_dni > 7:
            cena = pocet_dni * 300

        return f"Cena výpůjčky je {cena}."


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47543)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

while True:
    znacka = input("Jakou značku si chcete půjčit? ")
    if znacka == "Peugeot":
        print(auto1.get_info())
        auto1.pujc_auto()
    elif znacka == "Škoda":
        print(auto2.get_info())
        auto2.pujc_auto()
    else:
        print("Nemáme.")
        break

print(auto1.vrat_auto(1234567, 8))


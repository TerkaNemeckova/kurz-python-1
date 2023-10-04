sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod_soucastky = input("Zadejte kod soucastky: ")
mnozstvi = int(input("Zadejte množství: "))

if kod_soucastky not in sklad: 
    print ("Daná součástka není skladem.")
else:
    if mnozstvi > sklad[kod_soucastky]:
        print(f"Na skladě není dostatek zásob, lze prodat pouze {sklad[kod_soucastky]} kusů.")
        odebrano = sklad.pop(kod_soucastky)
        print(f"Ze skladu bylo odebráno {odebrano} kusů.")
    else:
        print(f"Na skladě je dostatek zásob, bude Vám vydáno {mnozstvi} kusů.")
        sklad[kod_soucastky] = sklad[kod_soucastky] - mnozstvi
        print(f"Aktuální množství položky {kod_soucastky} je {sklad[kod_soucastky]}.")
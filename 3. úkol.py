import json

# otevření souboru s body
with open('body.json', mode="r", encoding='utf-8') as file:
    studenti_body = json.load(file)

# příprava prázdného slovníku
znamky = {}

# do slovníku známky vkládám pass, fail
for jmeno, body in studenti_body.items():
    if body >= 60:
        znamky[jmeno] = "Pass"
    else: 
        znamky[jmeno] = "Fail"

# uložení do souboru
with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(znamky, file)

# otevření souboru bonusy
with open('bonusy.json', mode="r", encoding='utf-8') as file:
    bonusy = json.load(file)

# přičtení bonusů k původním bodům
for jmeno, bonus in bonusy.items():
    studenti_body[jmeno] = studenti_body[jmeno] + bonus


# vytvoření nového slovníku
hodnoceni = {}

for jmeno, body in studenti_body.items():
    if body >= 90:
        hodnoceni[jmeno] = "1"
    elif body >= 70 and body < 89:
        hodnoceni[jmeno] = "2"
    elif body >= 50 and body < 69:
        hodnoceni[jmeno] = "3"
    elif body >= 30 and body < 49:
        hodnoceni[jmeno] = "4"
    else:
        hodnoceni[jmeno] = "5"

with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(hodnoceni, file)
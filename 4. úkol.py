from math import ceil

def platnost_čísla(cislo):
    if (len(cislo) == 9 and cislo.isdigit()) or (len(cislo) == 13 and cislo[:4] == "+420" and cislo[1:].isdigit()):
        return True
    else:
        return False
    
def cena_zpravy(zprava):
    pocet_znaku = len(zprava)
    pocet_sms = ceil(pocet_znaku / 180)
    cena = pocet_sms * 3
    return cena

telefonni_cislo = input("Zadej telefonní číslo: ")
platnost_telefonniho_cisla = platnost_čísla(telefonni_cislo)

if platnost_telefonniho_cisla == True:
    text_sms = input("Vaše zpráva: ")
    cena_sms = cena_zpravy(text_sms)
    print("SMS bude stát " + str(cena_sms) + " Kč")
else:
    print("Špatně zadané číslo!")
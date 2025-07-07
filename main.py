"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Pavol Medo
email: palimedo@gmail.com
"""

import random
import time

########## Pozdrav uživatele a úvodní text ##########
cara = "-" * 50
print(
f"""
Ahoj!
{cara}
Vytvořil jsem pro tebe 4 místné náhodné číslo.
Pojďme hrát hru Bulls & Cows.
{cara}
""", end=""
)

########## Funkce pro generování čísla ##########
def vygeneruj_cislo():
    cisla = list("0123456789")
    while True:
        nahodna_cisla = random.sample(cisla, 4)
        if nahodna_cisla[0] != "0":
            return "".join(nahodna_cisla)

########## Funkce pro validaci tipu uživatele ##########
def validuj_tip(tip):
    """
    Ověří platnost uživatelského tipu.

    Podmínky platnosti:
    - Tip musí obsahovat 4 čísla.
    - Nesmí začínat 0.
    - Musí obsahovat jen čísla.
    - Čísla se nesmí opakovat.

    :param tip: Řetězec/ hráčův tip.
    :type tip: str
    :return: True, pokud je tip platný, jinak False.
    :rtype: bool
    """
    if tip[0] == "0":
        print("Číslo nesmí začínat nulou.")
        return False
    if not tip.isnumeric():
        print("Zadej pouze čísla.")
        return False
    if len(tip) != 4:
        print("Číslo musí mít 4 číslice.")
        return False
    if len(set(tip)) != 4:
        print("Čísla se nesmí opakovat.")
        return False
    return True

########## Funkce pro porovnání tipu s tajným číslem ##########
def porovnej_tip(tip, tajne_cislo):
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    return bulls, cows

########## Funkce pro formátování výsledku ##########
def formatuj_vysledek(bulls, cows):
    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bulls_text}, {cows} {cows_text}"

########## Hlavní část programu ##########
tajne_cislo = vygeneruj_cislo()
pocet_pokusu = 0

start = time.time()

while True:
    tip = input("Zadej číslo: ")
    if validuj_tip(tip):
        pocet_pokusu += 1
        bulls, cows = porovnej_tip(tip, tajne_cislo)
        if bulls == 4:
            end = time.time()
            cas = end - start
            minuty = int(cas // 60)
            sekundy = round(cas % 60, 2)
            print(f"Správně! Uhodl jsi číslo {tajne_cislo} na {pocet_pokusu}. pokus!")
            print(f"Trvalo ti to {minuty} minut a {sekundy} sekund.")
            break
        else:
            print(formatuj_vysledek(bulls, cows))
            print(cara)
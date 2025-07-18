"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Pavol Medo
email: palimedo@gmail.com
"""

import random
import time

########## Konstanty ##########

delka_cisla = 4
cara = "-" * 50

########## Funkce ##########

def vygeneruj_cislo() -> str:
    """
    Vygeneruje náhodné čtyřmístné číslo s unikátními číslicemi,
    které nezačíná nulou.

    :return: Tajné čtyřmístné číslo.
    :rtype: str
    """
    cisla = list("0123456789")
    while True:
        nahodna_cisla = random.sample(cisla, delka_cisla)
        if nahodna_cisla[0] != "0":
            return "".join(nahodna_cisla)

def validuj_tip(tip: str) -> bool:
    """
    Ověří platnost uživatelského tipu.

    Podmínky:
    - Musí mít správnou délku.
    - Nesmí být prázdný.
    - Musí obsahovat pouze čísla.
    - Nesmí začínat nulou.
    - Musí mít unikátní číslice.

    :param tip: Hráčův tip.
    :type tip: str
    :return: True, pokud je platný, jinak False.
    :rtype: bool
    """
    if len(tip) != delka_cisla:
        print(f"Číslo musí mít {delka_cisla} číslice.")
        return False
    if not tip.isnumeric():
        print("Zadej pouze čísla.")
        return False
    if tip[0] == "0":
        print("Číslo nesmí začínat nulou.")
        return False
    if len(set(tip)) != delka_cisla:
        print("Čísla se nesmí opakovat.")
        return False
    return True

def porovnej_tip(tip: str, tajne_cislo: str) -> tuple[int, int]:
    """
    Porovná tip s tajným číslem a vrátí počet býků a krav.

    :param tip: Tip hráče.
    :type tip: str
    :param tajne_cislo: Tajné číslo.
    :type tajne_cislo: str
    :return: Počet býků a krav.
    :rtype: tuple[int, int]
    """
    byci = 0
    kravy = 0
    for index, znak in enumerate(tip):
        if znak == tajne_cislo[index]:
            byci += 1
        elif znak in tajne_cislo:
            kravy += 1
    return byci, kravy

def vypis_vysledek(byci: int, kravy: int) -> None:
    """
    Vytiskne výsledek porovnání.

    :param byci: Počet býků.
    :param kravy: Počet krav.
    """
    byci_text = "býk" if byci == 1 else "býci"
    kravy_text = "kráva" if kravy == 1 else "krávy"
    print(f"{byci} {byci_text}, {kravy} {kravy_text}")
    print(cara)

########## Hlavní herní smyčka ##########

def hra() -> None:
    """
    Spustí hlavní smyčku hry Býci & Krávy.
    """
    print(
        f"""
Ahoj!
{cara}
Vytvořil jsem pro tebe {delka_cisla} místné náhodné číslo.
Pojďme hrát hru Býci & Krávy.
{cara}
""", end=""
    )

    tajne_cislo = vygeneruj_cislo()
    pocet_pokusu = 0
    start = time.time()

    while True:
        tip = input("Zadej číslo: ").strip()
        if not tip:
            print("Vstup nesmí být prázdný.")
            continue
        if validuj_tip(tip):
            pocet_pokusu += 1
            byci, kravy = porovnej_tip(tip, tajne_cislo)
            if byci == delka_cisla:
                konec = time.time()
                cas = konec - start
                minuty = int(cas // 60)
                sekundy = round(cas % 60, 2)
                print(f"Správně! Uhodl jsi číslo {tajne_cislo} na {pocet_pokusu}. pokus!")
                print(f"Trvalo ti to {minuty} minut a {sekundy} sekund.")
                break
            else:
                vypis_vysledek(byci, kravy)

########## Spuštění hry ##########

if __name__ == "__main__":
    hra()
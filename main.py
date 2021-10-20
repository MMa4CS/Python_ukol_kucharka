# importy pythonovských knihoven
# import datetime
# import time
from dateutil.relativedelta import relativedelta
import sys

# importy mých knihovniček/skriptů
import parsovani
from validace import *
from estetika import *
from recepty import *
from texty import *
from parsovani import *


def hlavni_funkce():
    print(text_estet(uvitani, "="))  # slušně uvítám uživatele...

    # zadání a kontrola jména
    jmeno = input(vyzva_jmeno)
    while not text_validace(jmeno):
        print(chyba_zadani)
        jmeno = input(vyzva_jmeno)

    # zadání a kontrola příjmení
    prijmeni = input(vyzva_prijmeni)
    while not text_validace(prijmeni):
        print(chyba_zadani)
        prijmeni = input(vyzva_prijmeni)

    # zadání a kontrola e-mailu
    emailova_adresa = input(vyzva_email)
    while not email_validace(emailova_adresa):
        print(chyba_zadani)
        emailova_adresa = input(vyzva_email)

    # zadání a kontrola data narození že je to parsovatelný text
    datum_narozeni = input(vyzva_datum_narozeni)
    while not datum_vstup_validace(datum_narozeni):
        print(chyba_zadani)
        datum_narozeni = input(vyzva_datum_narozeni)

    # ověření věku, když věk uživatel nesplňuje, tak ukončím aplikaci po stisknutí enteru
    vek = relativedelta(datetime.datetime.now().date(), parsovani.text_na_datum(datum_narozeni)).years
    if vek >= 12:
        print(spravne_udaje)
        print(popis_uzivatele(jmeno, prijmeni, emailova_adresa, vek))
        print(text_estet("", "-"))
    else:
        print(mlady_uzivatel)
        input()
        sys.exit()

    # hlavní smyčka programu - uživatel prošel, tak teď si může říkat o recepty...
    while True:
        pozadavek_zakaznika = input(vyzva_recept)

        if pozadavek_zakaznika in seznam_receptu:
            print(seznam_receptu[pozadavek_zakaznika])
            print(text_estet("", "-"))
        elif pozadavek_zakaznika in ["k", "K"]:
            sys.exit()
        else:
            print(spatny_vyber)


# no a teď už jen zavolat ten svůj výtvor...
hlavni_funkce()

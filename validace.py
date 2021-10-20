import datetime


def text_validace(text: str) -> bool:
    """tato fce kontroluje text zda je to čistý a-text a vrací boolean
    :rtype: object
    """
    if text.isalpha():
        return True
    else:
        return False


def email_validace(email: str) -> bool:
    """tato fce kontroluje emailovou adresu na strukturu adresy a vrací boolean"""
    # kontrola na délku e-mailu
    if len(email) >= 6:
        pass
    else:
        return False

    # kontrla na pouze 1x@ v e-mailu
    acount = 0
    for i in email:
        if i == "@":
            acount += 1
    if acount == 1:
        pass
    else:
        return False

    # kontrola na první znak zadaného emailu
    if email[0] not in "._-@" and email[len(email) - 1] not in "._-@":
        pass
    else:
        return False

    # kontrola znaků v emailu
    for i in email:
        if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@":
            pass
        else:
            return False

    # kontrola alespoň na jednu tečku v e-mailu
    if "." in email:
        pass
    else:
        return False

    return True


def datum_vstup_validace(datum: str) -> bool:
    """tato fce kontroluje text zadaný jako datum na znaky a správný počet teček a vrací boolean"""
    # kontrola na délku vstupu 8 - 10 znaků
    if 8 <= len(datum) <= 10:
        pass
    else:
        return False

    # kontrola na znaky
    pocet_tecek = 0

    for i in datum:
        if i in "0123456789.":
            if i == ".":
                pocet_tecek += 1
        else:
            return False

    if pocet_tecek == 2:
        pass
    else:
        return False

    return True


def vek_validace(narozeni: datetime) -> bool:
    """tato fce kontroluje věk oproti aktuálnímu datumu a vrací boolean"""
    dnes = datetime.datetime.today()

    if narozeni - dnes >= 12:
        return True
    else:
        return False

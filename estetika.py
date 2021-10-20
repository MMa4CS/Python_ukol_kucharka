def text_estet(text: str, znak: str, delka: int = 50) -> str:
    """Fce naformatuje text, v pripade znaku '=' prida podtrzeni i nadtrzeni, v pripade jakehokoliv jineho znaku
    text jen podtrhne v zadane delce, pokud je zadana"""
    if znak == "=":
        return len(text) * "=" + "\n" + text + "\n" + len(text) * "=" + "\n"
    else:
        return delka * znak


def popis_uzivatele(jmeno: str, prijmeni: str, email: str, vek: int) -> str:
    """Fce vrací string s popisem zákazníka včetně naformátování velkých prvních písmen u jména a příjmení a zobrazení
    emailu malými písmeny - v případě, že uživatel nerozlišoval, nebo špatně rozlišoval malá a velká písmena."""

    return f"Jmenuješ se {jmeno.title()} {prijmeni.title()}, tvůj e-mail je {email.lower()} a je ti {vek} let."

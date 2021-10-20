import datetime


def text_na_datum(text: str) -> datetime.date:
    den, mesic, rok = text.split(".")
    return datetime.date(int(rok), int(mesic), int(den))

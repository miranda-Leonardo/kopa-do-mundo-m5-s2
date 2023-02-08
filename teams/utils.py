from datetime import datetime
from rest_framework.views import Response, status


class NegativeTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message: str):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


def data_processing(data: dict):
    if data["titles"] < 0:
        raise NegativeTitlesError({"error": "titles cannot be negative"})

    first_cup = datetime.strptime(data["first_cup"], "%Y-%m-%d")
    first_cup = first_cup.strftime("%Y")

    diference = int(first_cup) - 1930
    if diference < 0 or diference % 4 != 0:
        raise InvalidYearCupError({"error": "there was no world cup this year"})

    if diference / 4 > data["titles"]:
        raise ImpossibleTitlesError({"error": "impossible to have more titles than disputed cups"})

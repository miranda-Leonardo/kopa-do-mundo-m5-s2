from datetime import datetime


class NegativeTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message: str):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


def valid_titles(titles: str) -> None:
    if titles >= 0:
        return

    raise NegativeTitlesError("titles cannot be negative")


def valid_first_cup(first_cup: str) -> None:
    first_cup = datetime.strptime(first_cup, "%Y-%m-%d")
    first_cup = first_cup.strftime("%Y")

    diference = int(first_cup) - 1930
    if diference >= 0 and diference % 4 == 0:
        return

    raise InvalidYearCupError("there was no world cup this year")


def valid_titles_year(titles: str, first_cup: str) -> None:
    first_cup = datetime.strptime(first_cup, "%Y-%m-%d")
    first_cup = first_cup.strftime("%Y")

    diference = int(first_cup) - 1930
    if diference / 4 <= titles:
        return

    raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


def data_processing(data: dict) -> str:
    try:
        valid_titles(data["titles"])
        valid_first_cup(data["first_cup"])
        valid_titles_year(data["titles"], data["first_cup"])
    except NegativeTitlesError as err:
        return err.message
    except InvalidYearCupError as err:
        return err.message
    except ImpossibleTitlesError as err:
        return err.message

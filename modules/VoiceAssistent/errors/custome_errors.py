class DidNotUnderstand(Exception):
    def __str__(self) -> str:
        return "I didn't understand what you said"


class CannotOpenApplication(Exception):
    def __str__(self) -> str:
        return "Couldn't open specified application"


class CannotCloseApplication(Exception):
    def __str__(self) -> str:
        return "Couldn't close specified application"


class CannotSearchOnInternet(Exception):
    def __str__(self) -> str:
        return "Couldn't search given text on Internet"

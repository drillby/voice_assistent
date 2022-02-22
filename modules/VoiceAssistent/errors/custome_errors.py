class DidNotUnderstand(Exception):
    def __str__(self):
        return "I didn't understand what you said"


class CannotOpenApplication(Exception):
    def __str__(self):
        return "Couldn't open specified application"


class CannotCloseApplication(Exception):
    def __str__(self):
        return "Couldn't close specified application"

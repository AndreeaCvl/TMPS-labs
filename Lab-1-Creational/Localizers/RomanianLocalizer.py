# factory method for Romanian translation
class RomanianLocalizer:
    def __init__(self):
        self.translations = {"The Master and Margarita": "Maestrul și Margarita",
                             "I, Robot": "Eu, Robotul",
                             "The Book of Sand": "Cartea de nisip"}

    def localize(self, msg):
        return self.translations.get(msg, msg)
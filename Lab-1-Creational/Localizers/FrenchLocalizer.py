# factory method for French translation
class FrenchLocalizer:
    def __init__(self):
        self.translations = {"The Master and Margarita": "Le maître et Marguerite",
                             "I, Robot": "Les Robots",
                             "The Book of Sand": "Le Livre de Sable "}

    def localize(self, msg):
        return self.translations.get(msg, msg)
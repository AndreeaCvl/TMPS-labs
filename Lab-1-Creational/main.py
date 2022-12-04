from Library import Library
from Localizers.EnglishLocalizer import EnglishLocalizer
from Localizers.FrenchLocalizer import FrenchLocalizer
from Localizers.RomanianLocalizer import RomanianLocalizer
from Book import Book
from AdultBooks import AdultBooks
from ChildrenBooks import ChildrenBooks
from PublisherCache import PublisherCache

if __name__ == '__main__':

    # contains dict with the classes implementing factory method. Used to add a new feature (translation).
    def Factory(language="English"):
        """Factory Method"""
        localizers = {
            "French": FrenchLocalizer,
            "English": EnglishLocalizer,
            "Romanian": RomanianLocalizer,
        }

        return localizers[language]()

    # the parameters of both classes will change when updating any of the objects of type Library because
    # the class Library follows the Singleton Pattern
    library = Library()
    new_library = Library()
    new_library.lib_name = "My library"

    # creating objects of type book. following 2 patterns at a time - Builder pattern (see class Book for more details)
    # and abstract factory
    print()
    book = Book(AdultBooks) # AdultBooks is a class containing the target of our book (abstract factory pattern)

    # adding data about the new book using the builder pattern. The values of the hyperparameters are modified
    # using functions such as set_name, set_author, etc.
    book.set_name("The Master and Margarita")
    book.set_author("Bulgakov")
    book.set_cover("Hardcover")
    book.set_library(library)
    book.display()

    print()

    # translating the name of the book in Romanian using factory methhod.
    # good because for creating the new type of object, the client uses the same common interface
    language = Factory("Romanian")
    book.set_name(language.localize(book.name))
    book.display()
    print()

    # prints the audience of a book - adult or children. Abstract factory method
    book.show_target()

    print()
    print()

    # creating objects of type book. following 2 patterns at a time - Builder pattern (see class Book for more details)
    # and abstract factory
    book2 = Book(ChildrenBooks)
    book2.set_name("A children book")
    book2.set_author("Kant")
    book2.set_cover("Hardcover")
    book2.set_library(library)

    book2.display()
    print()
    book2.show_target()

    print()

    # prototype method
    # allows making clones of objects
    print("PROTOTYPE METHOD")
    print()
    PublisherCache.load() # initializing the classes from the Genres directory via PublisherCache

    # the genre of the first book is fiction. It was published in 2004.
    fiction = PublisherCache.get_book("1") # id=1, fiction
    fiction.set_title(book.name)
    fiction.set_year(2004)
    print(fiction.get_type())
    print(fiction.get_title())
    print(fiction.get_year())

    print()

    # this book has the same title and type as the previous one, but it was published in 2010.
    # the code above makes a clone and just updates the year
    fiction2 = fiction.clone()
    fiction2.set_year(2010)
    print(fiction2.get_type())
    print(fiction2.get_title())
    print(fiction2.get_year())

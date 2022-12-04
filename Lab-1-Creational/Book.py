# "has a" relationship between Library and Book
# implements builder pattern and abstract factory method
class Book:
    def __init__(self, age_factory=None):
        self.name = None
        self.author = None
        self.cover = None
        self.library = None

        # abstract factory. age_factcory is a class received as a parameter which contains the target audience of a book
        self.age_factory = age_factory

    def show_target(self):
        # creates and shows the target of a book using the abstract factory
        target = self.age_factory()
        print(f'The book is for {target}')

    # builder pattern
    # there are specific functions created for adding new components to our object (title, author, cover...)
    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_cover(self, cover):
        self.cover = cover

    def set_library(self, lib):
        self.library = lib.lib_name

    def display(self):
        print('Library: ', self.library)
        print('Title: ', self.name)
        print("Author:", self.author)
        print("Cover:", self.cover)

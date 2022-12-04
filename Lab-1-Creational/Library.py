# singleton class
# no matter how many objects of type Library there are in our code, they are the same object and changing one of them
# produces a change in all other objects too. 
class Library:
    def __new__(lib):
        if not hasattr(lib, 'instance'):
            lib.instance = super(Library, lib).__new__(lib)
        return lib.instance
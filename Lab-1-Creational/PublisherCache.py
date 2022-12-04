from Genres.Fiction import Fiction
from Genres.Poetry import Poetry
from Genres.Essay import Essay


# implements prototype method
# function load find the genre of a book by id
class PublisherCache:
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_book(sid):
        book = PublisherCache.cache.get(sid, None)
        return book.clone()

    @staticmethod
    def load():
        fiction = Fiction()
        fiction.set_id("1")
        PublisherCache.cache[fiction.get_id()] = fiction

        poetry = Poetry()
        poetry.set_id("2")
        PublisherCache.cache[poetry.get_id()] = poetry

        essay = Essay()
        essay.set_id("3")
        PublisherCache.cache[essay.get_id()] = essay

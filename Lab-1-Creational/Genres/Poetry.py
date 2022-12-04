from PublisherBooks import PublisherBooks


# fiction genre class (abstract factory method)
class Poetry(PublisherBooks):
    def __init__(self):
        super().__init__()
        self.type = "Poetry"

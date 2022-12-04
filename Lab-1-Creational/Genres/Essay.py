from PublisherBooks import PublisherBooks


# essay genre class (abstract factory method)
class Essay(PublisherBooks):
    def __init__(self):
        super().__init__()
        self.type = "Essay"

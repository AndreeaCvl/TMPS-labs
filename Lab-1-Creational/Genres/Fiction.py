from PublisherBooks import PublisherBooks


# fiction genre class (abstract factory method)
class Fiction(PublisherBooks):
    def __init__(self):
        super().__init__()
        self.type = "Fiction"

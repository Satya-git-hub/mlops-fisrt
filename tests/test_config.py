import Exception

class NotInRange(Exception):
    def __init__(self, message = "Value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a=1
    b=1
    assert a==b
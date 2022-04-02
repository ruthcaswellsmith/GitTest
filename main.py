#  This is a simple python script to test git workflow

class Test:
    def __init__(self):
        self.a = 25
        self.b = 10


class Feature1:
    def __init__(self):
        pass

    @property
    def name(self):
        return "Feature 1"


if __name__ == "__main__":

    test = Test()
    print(test.a, test.b)

    feature1 = Feature1()
    print(feature1.name)


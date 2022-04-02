from new_feature2 import NewFeature2
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


class Feature2:
    def __init__(self):
        pass

    @property
    def name(self):
        return 'Feature 2'


if __name__ == "__main__":

    test = Test()
    print(test.a, test.b)

    feature1 = Feature1()
    print(feature1.name)

    feature2 = Feature2()
    print(feature2.name)

    new_feature2 = NewFeature2()
    print(new_feature2.name)
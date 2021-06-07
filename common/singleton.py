"""
    question: how to make a singleton class in Python?

"""


class SingletonExample(object):

    def __new__(cls, *args, **kwargs):
        if "__instance__" in cls.__dict__:
            result = cls.__instance__
            print("already have instance {}".format(result))
            print(result.get_num())
            return cls.__instance__
        instance = super(SingletonExample, cls).__new__(cls)
        setattr(cls, "__instance__", instance)
        return instance

    def __init__(self, num):
        self.num = num

    def get_num(self):
        return self.num


if __name__ == '__main__':
    s1 = SingletonExample(1)
    print(s1.get_num())
    s2 = SingletonExample(2)
    print(s2.get_num())


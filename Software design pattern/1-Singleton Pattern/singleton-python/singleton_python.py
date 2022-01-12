class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Hello")
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls, *args, **kwargs)
    # return super(Singleton,cls).__new__(cls,*args,**kwargs)


class A(object):
    def __new__(cls):
        print("Creating instance")
        # return super(A, cls).__new__(cls)

    # It is not called
    def __init__(self):
        print("Init is called")


if __name__ == '__main__':
    st1 = Singleton()
    st2 = Singleton()
    print(st1)
    print(st2)
    # A()

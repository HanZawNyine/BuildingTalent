# Python program to
# demonstrate __new__

# don't forget the object specified as base
# class A(object):
#     def __init__(self):
#         print("Init is called")
#
#     def __new__(cls):
#         print("Creating instance")
#         return super(A, cls).__new__(cls)


# Python program to
# demonstrate __new__

class A(object):
    def __new__(cls):
        print("Creating instance")

    # It is not called
    def __init__(self):
        print("Init is called")




if __name__ == '__main__':
    A()

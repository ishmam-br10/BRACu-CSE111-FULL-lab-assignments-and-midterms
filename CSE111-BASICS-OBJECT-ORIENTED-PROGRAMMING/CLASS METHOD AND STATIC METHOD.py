class my_class:
    user_name = 'ishmam'

    @classmethod
    def name(cls):
        print(my_class.user_name)
    @staticmethod
    def stat():
        print("Static method called")
    def method(self):
        print("method called")

my_class.name()
s1 = my_class()
s1.method()
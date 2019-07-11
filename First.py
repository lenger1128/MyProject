class MyClass:
    def __init__(self):
        self.name='WangYu'
    def speak(self):
        print ("My name is {}".format(self.name))

if(__name__=='__main__'):
    A=MyClass()
    A.speak()
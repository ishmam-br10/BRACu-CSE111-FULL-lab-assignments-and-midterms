class defenders:
    saga = "The Defenders"
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def details(self):
        print("Name: ", self.name , "Title: ", self.title, "Saga: ", defenders.saga)

    ## class method to update the defenders name I am not gonna add it into the code rather keep it commented out
    # @classmethod
    # def update_saga(cls, new_saga):
    #     cls.saga = new_saga

    @classmethod
    def from_string(cls, info):
        name, title = info.split("-") # takes like this Matt Murrdock- daredevil
        name = name.title()
        obj = cls(name, title) # here i am splitting this like this (matt murrdock, daredevil)
        return obj

#################### command line ################################

def1 = defenders("Frank Castle", "The Punisher")
def2 = defenders.from_string("matt murrdock-Daredevil")
## to the printeeeeeeeeeeeeeeeeee

def1.details()
def2.details()
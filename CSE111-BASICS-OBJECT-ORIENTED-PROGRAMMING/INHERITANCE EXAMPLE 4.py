class defenders:  # parents class for daredevil , punisher
    def protectors(self):
        print("The Defenders Saga")

class daredevil(defenders):          # child class of defenders
    def hells_kitchen(self):
        print("Matthew Murrdock the devil of Hell's Kitchen")

class punisher(defenders):                  #  child class of defenders
    def castle(self):
        print("Frank Castle is the punisher")

class elektra(daredevil):                   ## child class of daredevil
    def nachitos(self):
        print("Elektra Nachitos is a true anti hero")

################ command ######################
name = elektra()
name.hells_kitchen()

class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def changeId(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))

jane = Student("Jane", 10)
jane.print()
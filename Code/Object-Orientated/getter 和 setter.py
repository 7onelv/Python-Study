class School:

    def __init__(self):
        self._name = ''
    
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name 
    
school1 = School()
school2 = School()
school1.setName('MIT')
school2.setName('BU')
print(school1.getName(), school2.getName())

#PythonTheRPG
#Written by Dillon J.
#TBA

class Player:
    def __init__(self, name, isMage, isWarrior):
        self.name = name;
        self.isMage = isMage;
        self.isWarrior = isWarrior;

    def setName(self, name):
        self.name = name;

    def isMage(self, isMage):
        self.isMage = isMage;

    def isWarrior(self, isWarrior):
        self.isWarrior = isWarrior;


def Main():
    Dillon = Player("", False, True);
    Dillon.setName("Dillon");
    Damian = Player("", True, False);
    Damian.setName("Damian")
    print(Dillon.name, Damian.name);

Main();
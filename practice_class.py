class Unit:
    def __init_(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
    

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() 순서상에 문제가 있을 수 있기 때문에
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
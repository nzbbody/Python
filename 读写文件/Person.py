class Person:
    Age = 7
    
    def __init__(self):        
        self.Color = 'Yellow'

if __name__ == '__main__':
    personA = Person()
    personB = Person()
    print(personA.Color)
    print(personB.Color)
    print(Person.Age)
    print(personA.Age)
    print(personB.Age)


    personA.Color = 'White'
    personA.Age = 9   
    print(personA.Color)
    print(personB.Color)
    print(Person.Age)
    print(personA.Age)
    print(personB.Age)

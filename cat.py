class Cat():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def lie(self):
        print(self.name.title() + " is now liing")
    def meow(self):
        print(self.name.title() + " said meow!")
    def update_weight(self, difference):
        self.weight+=difference
        if difference>0:
            print(self.name.title() + " put on weight")
        elif difference <0:
            print(self.name.title() + " lost weight")
        else:
            print("ther is no difference")

my_cat = Cat("Lissa", 5, 5.5)
print("My cat's name is " + my_cat.name.title())
print("My cat's age is " + str(my_cat.age))
my_cat.lie()
my_cat.meow()
my_cat.update_weight(-0.1)
older_cat = Cat("Chuma", 12, 10)
print("My cat's name is " + older_cat.name.title())
print("My cat's age is " + str(older_cat.age))
older_cat.lie()
older_cat.meow()
older_cat.update_weight(1)
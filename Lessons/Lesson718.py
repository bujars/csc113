class Mario:
    def move(self):
        print('I am printing')

class Shroom:
    def eat_shroom(self):
        print('Now I am big')


#Inheritance does't necessarily mean "parent/child"
class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()


#order of inheritance matters
#Starts from the first class, then it inherits that method from the class, then goes to the second, then third, etc...

#so class BigMario(Shroom, Mario) //Is different from above (if you have them share methods, like constructors)



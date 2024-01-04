class animals():
        def e(self):
            print ("i'm an elephant")
        def l(self):
            print ("i'm a lion")
        def g(self):
            print ("i'm a gorilla")
        def r(self):
            print ("i'm a rabbit")

class animal_features(animals):
        def eat_sugarcane(self):
            print ("eating sugarcane")
        def roar(self):
            print ('roar,roar,roar!!!')
        def eat_bananas(self):
            print("eating bananas")
        def jump(self):
            print ("jumping")
rabbit=animal_features()
gorilla=animal_features()
lion=animal_features()
elephant=animal_features()

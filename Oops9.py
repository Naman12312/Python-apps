class Electronic_devices:
    popularity = 4
    no_of_features = 1
    def work(self):
        return f"I have a many work but less than phones."
class pocket_gadgets(Electronic_devices):
    popularity = 3
    no_of_features = 3
    def work(self):
        return f"I have a less work than electronic devices"
class phones(pocket_gadgets):
    popularity = 6
    no_of_features = 10000
    def work(self):
        return f"I have the most work of all."
Computer = Electronic_devices()
small_video_game = pocket_gadgets()
iphone = phones()
print("Computer:")
print("popularity")
print(Computer.popularity)
print("No of featues:")
print(Computer.no_of_features)
print("work:")
print(Computer.work())
print("Small video game:")
print("popularity")
print(small_video_game.popularity)
print("No of featues:")
print(small_video_game.no_of_features)
print("work:")
print(small_video_game.work())
print("iphone:")
print("popularity")
print(iphone.popularity)
print("no of features:")
print(iphone.no_of_features)
print("work")
print(iphone.work())



exit()
class Dad:
    cricket = 1
class Son(Dad):
    dance = 1  
    def isdance(self):
        return f"Yes i dance {self.dance} no of times!"
class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Jackson Yeah! " \
            f"Yes i dance very awesomely {self.dance} no of times!"

darry = Dad()
larry = Son()
Harry = Grandson()
print(Harry.isdance())
'''
Next: Public, Private & Protected Access Specifiers | Python Tutorials For Absolute Beginners In Hindi #63
'''
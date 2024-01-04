while 1:
    programing_platforms=['java','dotnet','python','c']
    print("programing_platforms=",programing_platforms)
    class programming_platforms():
        def java(self):
            print ("i make android apps")
        def Dotnet(self):
            print ("i make windows apps")
        def python(self):
            print ("i also make windows apps")
        def c(self):
            print("i also make windows apps")
        
    def about1():
        print ("i make android apps")
    def about2():
        print ("i make windows apps")
    def about3():
        print ("i also make windows apps")
    def about4():
        print ("i also make windows apps")
    
    g=str(input(""))
    if g=='java':
        about1()
    elif g=='dotnet':
        about2()
    elif g=='python':
        about3()
    elif g=='c':
        about4()

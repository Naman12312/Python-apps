x = [0,0,0,0,0,0,0,0,0] 
o = [0,0,0,0,0,0,0,0,0]
def sum1(a,b,c):
    return a+b+c
def main(x,o): 
     #0+
    print(f"""
    {'X' if x[0] else('O' if o[0] else 0)} | {'X' if x[1] else('O' if o[1] else 1)} | {'X' if x[2] else('O' if o[2] else 2)}
    ---|---|---
    {'X' if x[3] else('O' if o[3] else 3)} | {'X' if x[4] else('O' if o[4] else 4)} | {'X' if x[5] else('O' if o[5] else 5)} 
    ---|---|---
    {'X' if x[6] else('O' if o[6] else 6)} | {'X' if x[7] else('O' if o[7] else 7)} | {'X' if x[8] else('O' if o[8] else 8)}
    """)
def checkwin(x,o):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
    for win in wins:
        if sum1(x[win[0]],x[win[1]],x[win[2]])==3:
            print("X win")
            return 1

        elif sum1(o[win[0]],o[win[1]],o[win[2]])==3:
            print("O win")
            return 0
    return -1
turn = 1
while True:
    if turn==0:
        oturn = int(input("O's Turn: "))
        o[oturn] = 1
        
    main(x, o)
    if turn == 1:
        xturn = int(input("X's Turn: ")) 
        x[xturn] = 1
    

    main(x, o)
    cwin = checkwin(x, o)
    if cwin!=-1:
        x = [0,0,0,0,0,0,0,0,0] 
        o = [0,0,0,0,0,0,0,0,0]
        continue
    

    

    turn=1-turn
        
    

        

        
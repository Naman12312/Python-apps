
# draw color-filled square in turtle 
  
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
gi=int(input("enter the lenght of side of a square"))
 
col = str(input("Enter the color name or hex value of color(# RRGGBB): ")) 
  
# set the fillcolor 
t.fillcolor(col) 
  
# start the filling color 
t.begin_fill() 
  
# drawing the square of side s 
for _ in range(4): 
  t.forward(gi) 
  t.right(90) 
  
# ending the filling of the color 
t.end_fill() 

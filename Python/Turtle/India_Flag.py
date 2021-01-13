import turtle 
# Getting a Screen 
ws = turtle.Screen() 
# Defing a turtle Instance 
flagTurtle = turtle.Turtle() 
# initially penup() 
flagTurtle.penup() 
# Initially setting position  
flagTurtle.goto(-180, 60)     
  
  
  
# For First Rectangle and filling  
# Orange color to Rectangle 
  
flagTurtle.pendown() 
flagTurtle.begin_fill() 
flagTurtle.fillcolor("orange") 
flagTurtle.left(90) 
flagTurtle.forward(90) 
flagTurtle.right(90) 
flagTurtle.forward(400) 
flagTurtle.right(90) 
flagTurtle.forward(90) 
flagTurtle.right(90) 
flagTurtle.forward(400) 
flagTurtle.end_fill() 
  
  
  
# For Second Rectangle 
  
flagTurtle.left(90) 
flagTurtle.forward(90) 
flagTurtle.left(90) 
flagTurtle.forward(400) 
flagTurtle.left(90) 
flagTurtle.forward(90) 
flagTurtle.left(90) 
flagTurtle.forward(400) 
flagTurtle.left(90) 
flagTurtle.forward(90) 
  
  
  
# For Third Rectangle and filling  
# Green color to Rectangle 
  
flagTurtle.begin_fill() 
flagTurtle.fillcolor("green") 
flagTurtle.forward(90) 
flagTurtle.left(90) 
flagTurtle.forward(400) 
flagTurtle.left(90) 
flagTurtle.forward(90) 
flagTurtle.left(90) 
flagTurtle.forward(400) 
flagTurtle.end_fill() 
  
  
  
# For making Ashoka Chakra  
# At middle of the flag. 
# And coloring it Blue 
  
flagTurtle.penup() 
flagTurtle.goto(23, 32) 
flagTurtle.pendown() 
flagTurtle.begin_fill() 
flagTurtle.fillcolor("blue") 
flagTurtle.circle(20) 
flagTurtle.end_fill() 
  
  
# It helps to hold the screen  
turtle.done()

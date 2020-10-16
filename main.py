import turtle as trtl
trtl.speed(0)
trtl.shape("circle")
trtl.pensize(5)

#Draws a spiral
for spiral_space in range(10,150): 
  trtl.goto(0,0)
  trtl.left(5)
  trtl.forward(10+spiral_space*0.9)
  trtl.pendown()
  trtl.stamp()
  trtl.penup()

#Draws the x and y axes with 200 pixels in every direction
def draw_axes():
  #Centers at origin
  trtl.goto(0,0)
  trtl.setheading(0)

  #Draws y-axis
  trtl.pendown()
  trtl.forward(200)
  trtl.backward(400)
  trtl.forward(200)

  #draws x-axis
  trtl.right(90)
  trtl.forward(200)
  trtl.backward(400)

  #Center at origin
  trtl.goto(0,0)
  trtl.setheading(0)
draw_axes()
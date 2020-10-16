import turtle as trtl
trtl.speed(0)
trtl.shape("circle")
for spiral_space in range(10,150): 
  trtl.goto(0,)
  trtl.left(5)
  trtl.forward(10+spiral_space*0.9)
  trtl.pendown()
  trtl.stamp()
  trtl.penup()
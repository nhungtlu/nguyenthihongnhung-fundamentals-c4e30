# # # A square

# # from turtle import *
# # color('blue','yellow')
# # begin_fill()
# # for i in range(4):
# #     forward(200)
# #     left(90)
# # end_fill()
# mainloop()


# # # An equilateral triangle

# # from turtle import *
# # color('blue','yellow')
# # begin_fill()
# # for i in range(2):
# #     forward(200)
# #     left(120)
# # end_fill()
# mainloop()
# # # A circle

# # from turtle import *
# # color('blue','yellow')
# # begin_fill()
# #     circle(200)
# # end_fill()
# mainloop()

# # # Multi-circle

# # from turtle import*
# # speed(0.1)
# # color('blue')
# # for i in range(6):
# #     circle(100)
# #     left (60)
# mainloop()
# # # Even better

# # from turtle import*
# # speed(0.1)
# # color('blue')
# # for i in range(50):
# #     circle(100)
# #     left(60)
# #     right(50)
# mainloop()

# # # 1.
# # from turtle import*
# # speed(0.1)
# # color('red')
# # for i in range(5):
# #     left(30)
# #     forward(100)
# #     right(60)
# #     forward(100)
# #     right(120)
# #     forward(100)
# #     right(60)
# #     forward(100)
# #     right(60)
# mainloop()
# # # 2.

# # from turtle import *
# # speed(0.1)
# # color('blue','red')
# # for i in range(4):
# #     forward(100)
# #     left(90)
# # for canh in range (3,8):
# #     color ('red')
# #     for j in range(canh):
# #             forward(100)
# #             left(360/canh)
# # forward(100)
# # left(120)
# # forward(100)
# mainloop()


# # from turtle import *
# # speed(0.1)
# # stroke color('blue','red')
# # for i in range(4):
# #     forward(100)
# #     left(90)
# # for canh in range (3,8):
# #     color ('red')
# #     for j in range(canh):
# #             forward(100)
# #             left(360/canh)
# # forward(100)
# # left(120)
# # forward(100)
# mainloop()

# # from turtle import * 
# # speed(0.7)
# # colors = ('red', 'blue', 'brown', 'yellow', 'gray')
# # for i in range(3): 
# #     color(colors[0])
# #     forward(100)
# #     left(120)
# # for i in range(4): 
# #     color(colors[1])
# #     forward(100)
# #     left(90)
# # for i in range(5): 
# #     color(colors[2])
# #     forward(100)
# #     left(360/5)
# # for i in range(6): 
# #     color(colors[3])
# #     forward(100)
# #     left(360/6)
# # for i in range(7): 
# #     color(colors[4])
# #     forward(100)
# #     left(360/7)
# mainloop()

from turtle import *
colors = ['red','blue','brown','yellow','grey']
for a in colors:
    begin_fill()
    color(a)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    end_fill()
 
mainloop()

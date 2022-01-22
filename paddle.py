from turtle import Turtle

STEPS = 20

class Paddle(Turtle):

  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)   
    self.x_pos = position[0]
    self.y_pos = position[1]
    self.pu()
    self.update_pos()

  def update_pos(self):
    self.goto(self.x_pos, self.y_pos)
      
  def go_up(self):
    self.y_pos += STEPS
    self.update_pos()

  def go_down(self):
    self.y_pos -= STEPS
    self.update_pos()
  
  def normalize(self):
    self.color('white')

  def collision(self):
    self.color('red')

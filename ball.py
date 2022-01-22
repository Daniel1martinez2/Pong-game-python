from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.pu()
    self.shape("circle")
    self.color("white")
    self.x_pos = 0
    self.y_pos = 0
    self.x_dir = 1
    self.y_dir = 1
    self.move_speed = 0.1

  def move(self):
    self.x_pos += self.move_speed * self.x_dir
    self.y_pos += self.move_speed * self.y_dir
    self.goto(self.x_pos, self.y_pos)

  def bounce_x(self):
    self.x_dir *= -1
    self.move_speed += 0.1

  def bounce_y(self):
    self.y_dir *= -1

  def reset(self):
    self.x_pos = 0
    self.y_pos = 0
    self.goto(0, 0)
    self.bounce_x()
    self.move_speed = 0.1
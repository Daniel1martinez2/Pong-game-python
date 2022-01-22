from turtle import Turtle
class Score(Turtle):
  def __init__(self, position):
    super().__init__()
    self.score_number = 0
    self.color("white")
    self.pu()
    self.hideturtle()
    self.goto(position[0], position[1])
    self.update()

  def update(self):
    self.write(self.score_number, align="center", font=("Times New Roman", 84, "normal") )

  def increase_score(self):
    self.score_number += 1
    self.clear()
    self.update()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

pl_1 = Paddle((350, 0))
pl_2 = Paddle((-350, 0))

score_pl_1 = Score((80, 200))
score_pl_2 = Score((-80, 200))

ball = Ball()


screen.listen()
screen.onkey(key="Up", fun=pl_1.go_up)
screen.onkey(key="Down", fun=pl_1.go_down)

screen.onkey(key="w", fun=pl_2.go_up)
screen.onkey(key="s", fun=pl_2.go_down)

game_is_on = True

while game_is_on:
  screen.update()
  ball.move()

  if ball.x_pos > 380:
    # ball.bounce_x()
    ball.reset()
    score_pl_2.increase_score()

  if ball.x_pos < -380:
    ball.reset()
    score_pl_1.increase_score()
    
  if  ball.y_pos > 280 or ball.y_pos < -280:
    ball.bounce_y()

  # Detect collision with paddle right
  if ball.distance(pl_1) < 50 and ball.xcor() > 320:
    ball.bounce_x()
    pl_1.collision()
    screen.ontimer(pl_1.normalize, 250)
  
  if ball.distance(pl_2) < 50 and ball.xcor() > -330:
    ball.bounce_x()
    pl_2.collision()
    screen.ontimer(pl_2.normalize, 250)

screen.exitonclick()
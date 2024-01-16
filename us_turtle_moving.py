from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Indian State Game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

tim = Turtle()
tim.speed(2)

screen.title("US State Game")
state_list = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()

for i in range(len(state_list)):
    # tim.penup()
    tim.pensize(1)
    tim.color("red")
    tim.goto(x_cor[i], y_cor[i])
    tim.color("black")
    tim.write(state_list[i], font=("arial", 10, "bold"))
    tim.pendown()

screen.exitonclick()

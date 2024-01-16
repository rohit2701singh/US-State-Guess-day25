from turtle import Turtle, Screen
import pandas

tim = Turtle()
tim.color("black")
tim.hideturtle()
screen = Screen()
screen.title("US State Game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
STATE_LIST = (data["state"].to_list())
TOTAL_STATE = len(STATE_LIST)

# print(STATE_LIST)

correct_ans = []
while len(correct_ans) < TOTAL_STATE:
    answer_state = screen.textinput(title=f"{len(correct_ans)}/{TOTAL_STATE} States correct",
                                    prompt="what's another state name? type 'exit' to close.").title()
    if answer_state == "Exit":
        # print(correct_ans)
        not_guessed_state = []
        for state in STATE_LIST:
            if state not in correct_ans:
                not_guessed_state.append(state)
        # print(not_guessed_state)

        creating_csv = pandas.DataFrame(not_guessed_state)
        creating_csv.to_csv("state_to_learn.csv")
        break

    if answer_state in STATE_LIST:
        # print(state_name)
        state_index = STATE_LIST.index(answer_state)
        state_name = data[data.state == answer_state]
        print(state_name)
        correct_ans.append(state_name.state[state_index])   # or use .title()
        x_cor = int(state_name.x)
        y_cor = int(state_name.y)
        tim.penup()
        tim.goto(x_cor, y_cor)
        tim.pendown()
        tim.write(state_name.state[state_index])
        # or use tim.write(state_name.state.item()) .item() to get only item
        # tim.write(state_name.x.item()) to get the x coordinate only.

screen.exitonclick()

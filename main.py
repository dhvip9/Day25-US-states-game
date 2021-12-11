from turtle import Turtle, Screen
import pandas
import time

screen = Screen()
screen.title("U.S.A States Game")
screen.bgpic("blank_states_img.gif")

pointer = Turtle()
pointer.penup()
pointer.hideturtle()

state_file = pandas.read_csv("50_states.csv")

ans_list = list(state_file["state"])
wright_answer = []
while len(wright_answer) < 50:
    user_Answer = screen.textinput(title=f"{len(wright_answer)} / 50 State Correct",
                                   prompt="Enter State Name").title()
    if user_Answer == "Exit":
        remaining_state = [state for state in ans_list if state not in wright_answer]
        df = pandas.DataFrame(remaining_state)
        df.to_csv("state_to_learn.csv")
        break

    sort_data = state_file[state_file["state"] == user_Answer]
    if user_Answer in ans_list:
        pointer.setposition(float(sort_data["x"]), float(sort_data["y"]))
        pointer.write(user_Answer)
        wright_answer.append(user_Answer)
        time.sleep(0.9)

import turtle
import pandas

DATA_FILE = "50_states.csv"

def import_states_data():
    data = pandas.read_csv(DATA_FILE)
    return data


def show_state_on_map(state_name, x_coor, y_coor):
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.color("black")
    new_state.goto(x=x_coor, y=y_coor)
    new_state.write(state_name)

def show_missing_states():
    missing_states = pandas.read_csv("states_to_learn.csv")
    for state_row in missing_states.itertuples():
        show_state_on_map(state_row.state, int(state_row.x), int(state_row.y))

### initialization ###

screen = turtle.Screen()
screen.setup(width=850, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = import_states_data()
states_number = len(states_data.index)


### main game ###
score = 0
correct_answers = []

for _ in range(states_number):
    answer_state = screen.textinput(title=f"{score}/{states_number} States Correct", prompt="What's another state's name?")

    answer_state = answer_state.title()

    if answer_state == "Exit":
        filtered_states = states_data[~states_data.state.isin(correct_answers)]
        filtered_states.to_csv("states_to_learn.csv")
        break

    if states_data.state.str.contains(answer_state).any() and (answer_state not in correct_answers):
        correct_answers.append(answer_state)
        state_row = states_data[states_data.state == answer_state]
        show_state_on_map(answer_state, int(state_row.x), int(state_row.y))
        score += 1

show_missing_states()
screen.exitonclick()
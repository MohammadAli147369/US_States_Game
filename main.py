import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count = 0
guessed_state = []
data = pandas.read_csv("50_states.csv")


all_state = data.state.to_list()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's matter?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# save the learn.csv

for sta in all_state:
    if sta in guessed_state:
        all_state.remove(sta)

d = pandas.DataFrame(all_state)
d.to_csv("learn.csv")

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()

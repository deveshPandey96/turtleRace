from turtle import Turtle, Screen


screen = Screen()
screen.setup(width = 1000, height = 800)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
for turtle_index in range(0,7):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-480, 350-(100*turtle_index))


screen.exitonclick()

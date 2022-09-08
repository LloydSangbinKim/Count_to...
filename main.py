from turtle import Turtle, Screen
import time

score = Turtle()
screen = Screen()
score.hideturtle()
screen.setup(width=1500, height=1000)
gif = "abell46s-no.gif"
screen.title("Count to 100001")
screen.addshape(gif)
number = 1

progress_will_not_be_saved = Turtle()
progress_will_not_be_saved.hideturtle()
progress_will_not_be_saved.penup()
progress_will_not_be_saved.goto(570, 480)
progress_will_not_be_saved.write("progress will not be saved", font=("Arial", 10, "bold"))

game_is_on = True
while game_is_on:
    screen.bgcolor("white")
    time.sleep(0.1)
    count_to = Turtle()
    count_to.penup()
    count_to.hideturtle()
    count_to.write("COUNT TO...", align="center", font=("Arial", 100, "bold"))
    count_to.goto(0, 300)
    score.penup()
    score.goto(0, -300)
    score.write(f"{number - 1}", align="center", font=("Arial", 200, "bold"))
    answer_number = screen.textinput(title=f"Current Number: {number - 1}", prompt="Next Number: ")
    answer_number = int(answer_number)
    screen.update()
    if answer_number == number:
        number += 1
        screen.clear()
    elif answer_number != number:
        screen.clear()
        wrong_number = Turtle()
        wrong_number.hideturtle()
        wrong_number.write("Thats the wrong number!", align="center", font=("Arial", 40, "normal"))
        screen.bgcolor("red")
        time.sleep(1)
        break

total_score = Turtle()
total_score.hideturtle()
screen.clear()
total_score.write(f"Your Final Number Was: {number}", align="center", font=("Arial", 40, "normal"))

screen.mainloop()
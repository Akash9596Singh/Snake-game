from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open('highscore.txt', mode='r') as file:
            self.highscore = int(file.read())
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_score()
        # self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1

    def update_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.highscore))
        self.clear()
        self.write(f"Score: {self.score}    Highest Score: {self.highscore}", move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

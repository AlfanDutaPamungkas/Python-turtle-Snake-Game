from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCORE_DATA = "score.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.hideturtle()
        
        try:
            with open(SCORE_DATA, 'r') as file:
                pass
        except:
            self.check_dbase()

        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
        self.high_score()
        
    def high_score(self):
        with open(SCORE_DATA, "r") as file:
            new_highscore = file.read()
        
        if self.score >= int(new_highscore):
            with open(SCORE_DATA, "w", encoding = "utf-8") as file:
                file.write(str(self.score))
           
    def check_dbase(self):
        with open(SCORE_DATA, "w", encoding = "utf-8") as file:
            file.write(str(self.score))
         
    def update_scoreboard(self):
        with open(SCORE_DATA, "r") as file:
            self.highscore = file.read()
        self.write(f"Score : {self.score} Highscore : {self.highscore}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
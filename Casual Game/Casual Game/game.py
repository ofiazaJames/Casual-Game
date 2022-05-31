from tkinter import *
import random
import pygame
import openpyxl as xl

# Create the window and its size
root = Tk()
root.title("Food Frenzy")
root.iconbitmap("lunch-box.ico")
positionRight = int(root.winfo_screenwidth() / 2 - 400 / 2)
positionDown = int(root.winfo_screenheight() / 2.2 - 700 / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))
root.resizable(0, 0)

# Images

# Ingame Background
PHBG = PhotoImage(file="phbackground.png")
JPBG = PhotoImage(file="jpbackground.png")
FRBG = PhotoImage(file="frbackground.png")
HEART = PhotoImage(file="heart.png")

# Character
PLAYER = PhotoImage(file="player.png")

# PH Food
ADOBO = PhotoImage(file="adobo.png")
LECHON = PhotoImage(file="lechon.png")

# JP Food
RAMEN = PhotoImage(file="ramen.png")
SUSHI = PhotoImage(file="sushi.png")

# FR Food
BAGUETTE = PhotoImage(file="baguette.png")
CROISSANTS = PhotoImage(file="Croissants.png")

# ADDS ON FOOD
BOMB = PhotoImage(file="bomb.png")
VEGETABLES = PhotoImage(file="vegetables.png")

# MainMenu
MMBG = PhotoImage(file="mmbg.png")
PLAY = PhotoImage(file="mmplay.png")
PLAY1 = PhotoImage(file="mmplay1.png")
MM = PhotoImage(file="mainmenu.png")

MENU = PhotoImage(file="menu.png")
MENU1 = PhotoImage(file='menu1.png')
MMQUIT = PhotoImage(file="mmquit.png")
MMQUIT1 = PhotoImage(file="mmquit1.png")
MMPLAY = PhotoImage(file='play.png')
MMPLAY1 = PhotoImage(file='play1.png')
INSTRUCTIONS = PhotoImage(file="instructions.png")
INSTRUCTIONS1 = PhotoImage(file="instructions1.png")
INTRO = PhotoImage(file='intro.png')
INSTRUC = PhotoImage(file='instruc.png')
BACK = PhotoImage(file='back.png')
BACK1 = PhotoImage(file='back1.png')

# GameOVer
GAMEOVER = PhotoImage(file="gameover.png")
RETRY = PhotoImage(file="retry.png")
RETRY1 = PhotoImage(file='retry1.png')
QUIT = PhotoImage(file="quit.png")
QUIT1 = PhotoImage(file='quit1.png')

# HighScores
wb = xl.load_workbook('HighScores.xlsx')
sheet = wb['SHEET']
cell = sheet.cell(1, 1)


def mainGame():
    # Appearing MainGame
    canvas = Canvas(root, width=400, height=700)
    canvas.pack()
    root.update()

    # Food coordinates spawn
    startX = random.randint(40, 381)
    startY = random.randint(-100, 0)

    country = canvas.create_image(0, 0, image=FRBG, anchor=NW)

    # Character Image
    player_image = canvas.create_image(200, 700, image=PLAYER, anchor=S)

    # Food Images
    drawFood1 = canvas.create_image(startX, startY, image=BAGUETTE)
    drawFood2 = canvas.create_image(startX, startY, image=CROISSANTS)
    drawVegie = canvas.create_image(startX, startY, image=VEGETABLES)
    drawBomb = canvas.create_image(startX, startY, image=BOMB)
    drawHeart = canvas.create_image(30, 40, image=HEART)

    # Variables used
    global lives
    lives = 5
    global velocity
    velocity = 10
    global score
    score = 0

    heal = "heal.mp3"
    hurt = "explode.mp3"
    munch = "munch.mp3"
    missed = "hurt.mp3"
    PH = "phbg.mp3"
    JP = "jpbg.mp3"

    pygame.mixer.Channel(1).play(pygame.mixer.Sound('ingame.mp3'))

    # Creating labels in canvas
    player_score = canvas.create_text(320, 45, text="Score: " + str(score), font=('Times New Roman', 15, 'bold'))
    player_lives = canvas.create_text(60, 45, text="x" + str(lives), font=('Times New Roman', 15, 'bold'))

    # Different Functions
    def gameOver():
        global score
        highscore = cell.value
        pygame.mixer.Channel(1).stop()
        canvas.destroy()
        gameover = Canvas(root, width=400, height=700)
        gameover.pack()

        if score >= 0:
            gameover.create_image(0, 0, image=FRBG, anchor=NW)
        if score > 1000:
            gameover.create_image(0, 0, image=JPBG, anchor=NW)
        if score > 2000:
            gameover.create_image(0, 0, image=PHBG, anchor=NW)

        gameover.create_image(-58, -100, image=GAMEOVER, anchor=NW)
        gameover.create_text(200, 340, text="Score", font=('Helvetica', 30, 'bold'))
        gameover.create_text(200, 390, text=score, font=('Helvetica', 30, 'bold'))
        gameover.create_text(200, 230, text="High Score", font=('Helvetica', 30, 'bold'))
        HS = gameover.create_text(200, 280, text=highscore, font=('Helvetica', 30, 'bold'))

        if score > highscore:
            newScore = score
            cell.value = newScore
            wb.save('HighScores.xlsx')
            gameover.itemconfig(HS, text=newScore)

        def retry(event):
            gameover.destroy()
            mainGame()

        def shrink(event):

            pygame.mixer.music.load("pop.mp3")
            pygame.mixer.music.play(loops=0)
            btnretry1 = gameover.create_image(200, 450, image=RETRY1)
            gameover.tag_bind(btnretry1, "<Enter>", retry)

        def quit(event):
            root.destroy()

        def shrink1(event):
            pygame.mixer.music.load("pop.mp3")
            pygame.mixer.music.play(loops=0)
            btnquit1 = gameover.create_image(200, 650, image=QUIT1)
            gameover.tag_bind(btnquit1, "<Enter>", quit)

        def menu(event):
            gameover.destroy()
            mainmenus()

        def shrink2(event):

            pygame.mixer.music.load("pop.mp3")
            pygame.mixer.music.play(loops=0)
            btnmenu1 = gameover.create_image(200, 590, image=MENU1)
            gameover.tag_bind(btnmenu1, "<Enter>", menu)

        btnretry = gameover.create_image(200, 450, image=RETRY)
        gameover.tag_bind(btnretry, "<Button-1>", shrink)

        btnquit = gameover.create_image(200, 650, image=QUIT)
        gameover.tag_bind(btnquit, "<Button-1>", shrink1)

        btnmenu = gameover.create_image(200, 590, image=MENU)
        gameover.tag_bind(btnmenu, "<Button-1>", shrink2)

    def scoring(puntos):
        global score
        if lives > 0:
            score += puntos
            canvas.itemconfig(player_score, text="Score:" + str(score))

    def regen(buhay):
        global lives
        lives += buhay
        canvas.itemconfig(player_lives, text="x" + str(lives))

    def loseLife(bawas):
        global lives
        lives -= bawas
        if lives > 0:
            canvas.itemconfig(player_lives, text="x" + str(lives))
        else:
            gameOver()

    def audio(audio):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(audio))

    # Player Movement Functions
    def move_left(event):
        x = -10
        y = 0
        player_coord = canvas.coords(player_image)
        canvas.move(player_image, x, y)
        if player_coord[0] <= 40:
            canvas.coords(player_image, 40, 700)

    def move_right(event):
        x = 10
        y = 0
        player_coord = canvas.coords(player_image)
        canvas.move(player_image, x, y)
        if player_coord[0] >= 380:
            canvas.coords(player_image, 380, 700)

    # Food Movement Functions
    def food1_movement():
        global velocity
        global score
        respawnX = random.randint(40, 381)
        respawnY = random.randint(-450, 0)
        canvas.move(drawFood1, 0, velocity)
        food_coords = canvas.bbox(drawFood1)
        collision(drawFood1, random.randint(50, 100), 0, 0, munch)

        if food_coords[1] > 650:
            audio(missed)
            canvas.coords(drawFood1, respawnX, respawnY)
            loseLife(1)
            if score >= 1000:
                velocity = 15
            if score >= 2000:
                velocity = 20
            if score >= 3000:
                velocity = 25
        if score >= 1000:
            canvas.itemconfig(country, image=JPBG)
            canvas.itemconfig(drawFood1, image=RAMEN)
        if score >= 2000:
            canvas.itemconfig(country, image=PHBG)
            canvas.itemconfig(drawFood1, image=ADOBO)
        root.after(50, food1_movement)

    def food2_movement():
        global velocity
        global score
        respawnX = random.randint(40, 381)
        respawnY = random.randint(-450, 0)
        canvas.move(drawFood2, 0, velocity)
        food_coords = canvas.bbox(drawFood2)
        collision(drawFood2, random.randint(50, 100), 0, 0, munch)
        if food_coords[1] > 650:
            audio(missed)
            canvas.coords(drawFood2, respawnX, respawnY)
            loseLife(1)
            if score >= 1000:
                velocity = 15
            if score >= 2000:
                velocity = 20
            if score >= 3000:
                velocity = 25
        if score >= 1000:
            canvas.itemconfig(drawFood2, image=SUSHI)
        if score >= 2000:
            canvas.itemconfig(drawFood2, image=LECHON)
        root.after(50, food2_movement)

    def vegie_movement():
        global velocity
        respawnX = random.randint(40, 381)
        respawnY = random.randint(-450, 0)
        canvas.move(drawVegie, 0, velocity)
        food_coords = canvas.bbox(drawVegie)
        collision(drawVegie, 0, 1, 0, heal)
        if food_coords[1] > 650:
            canvas.coords(drawVegie, respawnX, respawnY)
            if score >= 1000:
                velocity = 15
            if score >= 2000:
                velocity = 20
            if score >= 3000:
                velocity = 25
        root.after(200, vegie_movement)

    def bomb_movement():
        global velocity
        respawnX = random.randint(40, 381)
        respawnY = random.randint(-450, 0)
        canvas.move(drawBomb, 0, velocity)
        food_coords = canvas.bbox(drawBomb)
        collision(drawBomb, 0, 0, 1, hurt)
        if food_coords[1] > 650:
            canvas.coords(drawBomb, respawnX, respawnY)
            if score >= 1000:
                velocity = 15
            if score >= 2000:
                velocity = 20
            if score >= 3000:
                velocity = 25
        if score <= 200:
            root.after(100, bomb_movement)
        else:
            root.after(50, bomb_movement)

    # Collision Events
    def collision(obj, points, life, decay, music):
        respawnX = random.randint(40, 381)
        respawnY = random.randint(-450, 0)
        player_loc = canvas.bbox(player_image)
        food_loc = canvas.bbox(obj)
        if (player_loc[1] < food_loc[3] < player_loc[3]) and (food_loc[2] > player_loc[0] > food_loc[0]):
            canvas.coords(obj, respawnX, respawnY)
            audio(music)
            regen(life)
            loseLife(decay)
            scoring(points)
        if (player_loc[2] > food_loc[0] > player_loc[0]) and (player_loc[1] < food_loc[3] < player_loc[3]):
            canvas.coords(obj, respawnX, respawnY)
            audio(music)
            regen(life)
            loseLife(decay)
            scoring(points)

            # Player Movements

    root.bind("<Left>", move_left)
    root.bind("<Right>", move_right)

    # Food Movements
    food1_movement()
    food2_movement()
    vegie_movement()
    bomb_movement()


# MainMenu Functions
def mainmenus():
    intro.destroy()
    # MainMenu Canvas
    mmcanvas = Canvas(root, width=400, height=700)
    mmcanvas.pack()
    mmcanvas.create_image(0, 0, image=MMBG, anchor=NW)
    instruction = Canvas(root, width=400, height=700)

    def mainmenu(event):
        def initmm():
            mmcanvas.pack_forget()
            pygame.mixer.music.stop()
            mainmenu = Canvas(root, width=400, height=700)
            mainmenu.pack()
            mainmenu.create_image(0, 0, image=MM, anchor=NW)

            def playnow(event):
                mainmenu.destroy()
                instruction.destroy()
                mainGame()

            def shrink1(event):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("pop.mp3")
                pygame.mixer.music.play(loops=0)
                mmbtnplay1 = mainmenu.create_image(199, 280, image=MMPLAY1)
                mainmenu.tag_bind(mmbtnplay1, "<Enter>", playnow)

            def backtomm(event):
                instruction.pack_forget()
                initmm()

            def shrink4(event):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("pop.mp3")
                pygame.mixer.music.play(loops=0)
                backbtn1 = instruction.create_image(30, 40, image=BACK1)
                instruction.tag_bind(backbtn1, "<Enter>", backtomm)

            def ins(event):
                mainmenu.destroy()
                instruction.configure(background='lightblue')
                instruction.pack()
                instruction.create_image(0, 50, image=INSTRUC, anchor=NW)
                backbtn = instruction.create_image(30, 40, image=BACK)
                instruction.tag_bind(backbtn, "<Button-1>", shrink4)

            def shrink2(event):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("pop.mp3")
                pygame.mixer.music.play(loops=0)
                btnins1 = mainmenu.create_image(199, 400, image=INSTRUCTIONS1)
                mainmenu.tag_bind(btnins1, "<Enter>", ins)

            def shrink3(event):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("pop.mp3")
                pygame.mixer.music.play(loops=0)
                btnquit1 = mainmenu.create_image(199, 520, image=MMQUIT1)
                mainmenu.tag_bind(btnquit1, "<Enter>", root.destroy())

            mmbtnplay = mainmenu.create_image(100, 180, image=MMPLAY, anchor=NW)
            mainmenu.tag_bind(mmbtnplay, "<Button-1>", shrink1)
            btnins = mainmenu.create_image(100, 300, image=INSTRUCTIONS, anchor=NW)
            mainmenu.tag_bind(btnins, "<Button-1>", shrink2)
            btnquit = mainmenu.create_image(100, 420, image=MMQUIT, anchor=NW)
            mainmenu.tag_bind(btnquit, "<Button-1>", shrink3)

        initmm()

    def shrink(event):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("pop.mp3")
        pygame.mixer.music.play(loops=0)
        btnplay1 = mmcanvas.create_image(200, 650, image=PLAY1)
        mmcanvas.tag_bind(btnplay1, "<Enter>", mainmenu)

    pygame.mixer.init()
    pygame.mixer.music.play(loops=100)
    btnplay = mmcanvas.create_image(200, 650, image=PLAY)
    mmcanvas.tag_bind(btnplay, "<Button-1>", shrink)


intro = Canvas(root, width=400, height=700)
intro.pack()
intro.create_image(0, 0, image=INTRO, anchor=NW)
root.after(3000, mainmenus)

root.mainloop()

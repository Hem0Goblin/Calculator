# Imports
import pygame
from math import sqrt
from tkinter import messagebox

# Initialize pyGame
pygame.init()

# Window and Resolution
RES = (450, 800)
win = pygame.display.set_mode(RES)

# Title
pygame.display.set_caption("Calculator Alpha")

# Icon
icon = pygame.image.load("calc.ico")
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

# Sounds
key = pygame.mixer.Sound("key.wav")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light_grey = (125, 125, 125)
light_light_grey = (180, 180, 180)
dark_grey = (50, 50, 50)
dark_dark_grey = (30, 30, 30)
orange = (150, 80, 0)
button_colors = (
    light_grey, light_grey, light_grey, orange, dark_grey, dark_grey, dark_grey, orange, dark_grey, dark_grey,
    dark_grey, orange, dark_grey, dark_grey, dark_grey, orange, dark_grey, dark_grey, dark_grey, orange)

# Font
font = pygame.font.SysFont('Arial', 30)


def show_storage(size_storage=70):
    global storage
    storage_font = pygame.font.SysFont("Arial", size_storage)
    storage_text = storage_font.render(storage, True, light_light_grey)
    if storage_text.get_width() <= 350:
        size_storage = 70
    elif storage_text.get_width() > 350:
        if size_storage == 30:
            pass
        size_storage -= 5
        storage_font = pygame.font.SysFont("Arial", size_storage)
        storage_text = storage_font.render(storage, True, light_light_grey)
        if size_storage <= 40:
            size_storage = 40
            pass
        elif storage_text.get_width() > 350:
            return show_storage(size_storage)
    length = len(storage)
    backup = storage[:]
    for i in range(len(storage)):
        if storage_text.get_width() > 350:
            storage = eval("'{0:." + str(length - i) + "g}'.format(float(storage))")
            storage_text = storage_font.render(storage, True, light_light_grey)
            if storage_text.get_width() < 350:
                break
            storage = backup[:]
    backup, storage = storage, backup
    if backup == "inf":
        raise OverflowError
    storage_text = storage_font.render(backup, True, light_light_grey)

    win.blit(storage_text,
             (storage_index[0] - storage_text.get_width(), storage_index[1] - storage_text.get_height() / 2))


def show_operator(size_operator=70):
    operator_font = pygame.font.SysFont("Arial", size_operator)
    operator_text = operator_font.render(operator, True, white)
    if operator_text.get_width() <= 50:
        size_operator = 70
    elif operator_text.get_width() > 50:
        size_operator -= 5
        if operator_text.get_width() > 50:
            return show_operator(size_operator)
    win.blit(operator_text, (operator_index[0], operator_index[1] - operator_text.get_height() / 2))


def show_input(size_input=70):
    global calculation_input
    input_font = pygame.font.SysFont("Arial", size_input)
    input_text = input_font.render(calculation_input, True, white)
    if input_text.get_width() <= 350:
        size_input = 70
    elif input_text.get_width() > 350:
        size_input -= 5
        input_font = pygame.font.SysFont("Arial", size_input)
        input_text = input_font.render(calculation_input, True, white)
        if size_input <= 40:
            size_input = 40
            pass
        elif input_text.get_width() > 350:
            return show_input(size_input)

    length = len(calculation_input)
    backup = calculation_input[:]
    for i in range(len(calculation_input)):
        if input_text.get_width() > 350:
            calculation_input = eval("'{0:." + str(length - i) + "g}'.format(float(calculation_input))")
            input_text = input_font.render(calculation_input, True, white)
            if input_text.get_width() < 350:
                break
            calculation_input = backup[:]

    backup, calculation_input = calculation_input, backup
    if backup == "inf":
        raise OverflowError
    input_text = input_font.render(backup, True, white)

    win.blit(input_text, (calculation_input_index[0] - input_text.get_width(),
                          calculation_input_index[1] - input_text.get_height() / 2))


# Texts
title = font.render("Calculator Beta", True, white)
button_texts = [font.render("x^y", False, black), font.render("x²", False, black), font.render(":)", True, black),
                font.render("÷", True, white), font.render("7", True, white), font.render("8", True, white),
                font.render("9", True, white), font.render("×", True, white), font.render("4", True, white),
                font.render("5", True, white), font.render("6", True, white), font.render("-", True, white),
                font.render("1", True, white), font.render("2", True, white), font.render("3", True, white),
                font.render("+", True, white), font.render("0", True, white), font.render(",", True, white),
                font.render("AC", True, white), font.render("=", True, white)]

# Images
sqrtimg = pygame.image.load("sqrt(x).png")

# Positions
storage_index = (400, 100)
calculation_input_index = (400, 200)
operator_index = (35, 150)
display_index = (25, 275)
button_num = 0
button_indexes = []
for row in range(5):
    for column in range(4):
        button_indexes.append((button_num, display_index))
        button_num += 1
        display_index = (display_index[0] + 100, display_index[1])
    display_index = (25, display_index[1] + 100)


# History
def savetohistory():
    pass


def loadhistory():
    pass


# Evaluate
calculation_input = "0"
operator = ""
storage = ""


def evaluate():
    global storage
    global calculation_input
    global operator
    if storage == "" and operator == "":
        storage = calculation_input
        calculation_input = "0"
        return ""
    if operator == "+" or operator == "-":
        storage = str(eval(str(storage) + operator + str(calculation_input)))
    elif operator == "×":
        storage = str(eval(str(storage) + "*" + str(calculation_input)))
    elif operator == "÷":
        if calculation_input == "0":
            messagebox.showerror("An Error Occured", "Zero Division Error!\nTry dividing with 1 if necessary\nAnd DON'T try to close tk window")
            return ""
        storage = str(eval(str(storage) + "/" + str(calculation_input)))
    elif operator == "x^y":
        storage = str(eval(str(storage) + "**" + str(calculation_input)))
    if operator == "x^2":
        if calculation_input == "0" and (storage == "" or storage == "0"):
            pass
        elif calculation_input != "0" and (storage == "" or storage == "0"):
            storage = str(float(calculation_input) ** 2)
            calculation_input = "0"
        else:
            calculation_input = storage
            storage = str(float(storage) ** 2)
            calculation_input = "0"
    if operator == "sqrt(x)":
        if storage == "" or storage == "0":
            if calculation_input == "0":
                print("1")
                pass
            elif calculation_input != "0":
                print("2")
                storage = str(sqrt(float(calculation_input)))
                calculation_input = "0"
        else:
            print("3")
            calculation_input = storage
            storage = str(sqrt(float(storage)))
            calculation_input = "0"


# Press Keys
press_counters16 = 0
press_counters12 = 0
press_counters13 = 0
press_counters14 = 0
press_counters8 = 0
press_counters9 = 0
press_counters10 = 0
press_counters4 = 0
press_counters5 = 0
press_counters6 = 0
press_countersBS = 0
press_countersDEL = 0
press_countersOP = 0
press_countersSOP = 0
press_countersENTR = 0


def press():
    global calculation_input, operator, storage
    global press_counters16, press_counters12, press_counters13, press_counters14, press_counters8, press_counters9
    global press_counters9, press_counters10, press_counters4, press_counters5, press_counters6
    global press_countersBS, press_countersDEL, press_countersOP, press_countersSOP, press_countersENTR

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicks = pygame.mouse.get_pressed(3)

    if keys[pygame.K_0] or keys[pygame.K_KP_0] \
            or (mouse_clicks[0] and ((((button_indexes[16][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[16][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters16 == 0 or press_counters16 > 15:
                calculation_input += "0"
                key.play()
            press_counters16 += 1
    else:
        press_counters16 = 0
    if keys[pygame.K_1] or keys[pygame.K_KP_1] \
            or (mouse_clicks[0] and ((((button_indexes[12][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[12][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters12 == 0 or press_counters12 > 15:
                calculation_input += "1"
                key.play()
            press_counters12 += 1
        elif calculation_input == "0":
            calculation_input = "1"
            key.play()
            press_counters12 += 1
            if press_counters12 == 0 or press_counters12 > 15:
                calculation_input += "1"
    else:
        press_counters12 = 0
    if keys[pygame.K_2] or keys[pygame.K_KP_2] \
            or (mouse_clicks[0] and ((((button_indexes[13][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[13][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters13 == 0 or press_counters13 > 15:
                calculation_input += "2"
                key.play()
            press_counters13 += 1
        elif calculation_input == "0":
            calculation_input = "2"
            key.play()
            press_counters13 += 1
            if press_counters13 == 0 or press_counters13 > 15:
                calculation_input += "2"
    else:
        press_counters13 = 0
    if keys[pygame.K_3] or keys[pygame.K_KP_3] \
            or (mouse_clicks[0] and ((((button_indexes[14][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[14][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters14 == 0 or press_counters14 > 15:
                calculation_input += "3"
                key.play()
            press_counters14 += 1
        elif calculation_input == "0":
            calculation_input = "3"
            key.play()
            press_counters14 += 1
            if press_counters14 == 0 or press_counters14 > 15:
                calculation_input += "3"
    else:
        press_counters14 = 0
    if keys[pygame.K_4] or keys[pygame.K_KP_4] \
            or (mouse_clicks[0] and ((((button_indexes[8][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[8][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters8 == 0 or press_counters8 > 15:
                calculation_input += "4"
                key.play()
            press_counters8 += 1
        elif calculation_input == "0":
            calculation_input = "4"
            key.play()
            press_counters8 += 1
            if press_counters8 == 0 or press_counters8 > 15:
                calculation_input += "4"
    else:
        press_counters8 = 0
    if keys[pygame.K_5] or keys[pygame.K_KP_5] \
            or (mouse_clicks[0] and ((((button_indexes[9][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[9][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters9 == 0 or press_counters9 > 15:
                calculation_input += "5"
                key.play()
            press_counters9 += 1
        elif calculation_input == "0":
            calculation_input = "5"
            key.play()
            press_counters9 += 1
            if press_counters9 == 0 or press_counters9 > 15:
                calculation_input += "5"
    else:
        press_counters9 = 0
    if keys[pygame.K_6] or keys[pygame.K_KP_6] \
            or (mouse_clicks[0] and ((((button_indexes[10][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[10][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters10 == 0 or press_counters10 > 15:
                calculation_input += "6"
                key.play()
            press_counters10 += 1
        elif calculation_input == "0":
            calculation_input = "6"
            key.play()
            press_counters10 += 1
            if press_counters10 == 0 or press_counters10 > 15:
                calculation_input += "6"
    else:
        press_counters10 = 0
    if keys[pygame.K_7] or keys[pygame.K_KP_7] \
            or (mouse_clicks[0] and ((((button_indexes[4][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[4][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters4 == 0 or press_counters4 > 15:
                calculation_input += "7"
                key.play()
            press_counters4 += 1
        elif calculation_input == "0":
            calculation_input = "7"
            key.play()
            press_counters4 += 1
            if press_counters4 == 0 or press_counters4 > 15:
                calculation_input += "7"
    else:
        press_counters4 = 0
    if keys[pygame.K_8] or keys[pygame.K_KP_8] \
            or (mouse_clicks[0] and ((((button_indexes[5][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[5][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters5 == 0 or press_counters5 > 15:
                calculation_input += "8"
                key.play()
            press_counters5 += 1
        elif calculation_input == "0":
            calculation_input = "8"
            key.play()
            press_counters5 += 1
            if press_counters5 == 0 or press_counters5 > 15:
                calculation_input += "8"
    else:
        press_counters5 = 0
    if keys[pygame.K_9] or keys[pygame.K_KP_9] \
            or (mouse_clicks[0] and ((((button_indexes[6][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[6][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if calculation_input != "0":
            if press_counters6 == 0 or press_counters6 > 15:
                calculation_input += "9"
                key.play()
            press_counters6 += 1
        elif calculation_input == "0":
            calculation_input = "9"
            key.play()
            press_counters6 += 1
            if press_counters6 == 0 or press_counters6 > 15:
                calculation_input += "9"
    else:
        press_counters6 = 0
    if keys[pygame.K_COMMA] or keys[pygame.K_KP_PERIOD] or keys[pygame.K_PERIOD] \
            or (mouse_clicks[0] and ((((button_indexes[17][1][0] + 50 - mouse_pos[0]) ** 2) +
                                      ((button_indexes[17][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
        if not ("." in calculation_input):
            calculation_input += "."
            key.play()

    if keys[pygame.K_BACKSPACE]:
        if len(calculation_input) == 1:
            calculation_input = "0"
            press_countersBS = 0
        elif calculation_input != "0":
            if press_countersBS == 0 or press_countersBS > 15:
                calculation_input = calculation_input[:-1]
                key.play()
            press_countersBS += 1
    else:
        press_countersBS = 0

    if (keys[pygame.K_DELETE] or (mouse_clicks[0] and
                                  ((((button_indexes[18][1][0] + 50 - mouse_pos[0]) ** 2) +
                                    ((button_indexes[18][1][1] + 50 - mouse_pos[
                                        1]) ** 2)) <= 1600))) and press_countersDEL == 0:
        calculation_input = "0"
        storage = ""
        operator = ""
        key.play()
        press_countersDEL += 1
    elif press_countersDEL > 0:
        if press_countersDEL == 15:
            press_countersDEL = -1
        press_countersDEL += 1

    if press_countersENTR == 0:
        if keys[pygame.K_EQUALS] or keys[pygame.K_KP_EQUALS] or keys[pygame.K_KP_ENTER] \
                or (mouse_clicks[0] and ((((button_indexes[19][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[19][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            key.play()
            evaluate()
            press_countersENTR += 1
    elif press_countersENTR > 0:
        if press_countersENTR == 8:
            press_countersENTR = -1
        press_countersENTR += 1

    if press_countersOP == 0:
        if keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS] \
                or (mouse_clicks[0] and ((((button_indexes[15][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[15][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            press_countersOP += 1
            key.play()
            evaluate()
            operator = "+"
            calculation_input = "0"
        elif keys[pygame.K_ASTERISK] or keys[pygame.K_KP_MULTIPLY] \
                or (mouse_clicks[0] and ((((button_indexes[7][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[7][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            press_countersOP += 1
            key.play()
            evaluate()
            operator = "×"
            calculation_input = "0"
        elif keys[pygame.K_SLASH] or keys[pygame.K_KP_DIVIDE] \
                or (mouse_clicks[0] and ((((button_indexes[3][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[3][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            press_countersOP += 1
            key.play()
            evaluate()
            operator = "÷"
            calculation_input = "0"
        elif keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS] \
                or (mouse_clicks[0] and ((((button_indexes[11][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[11][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            press_countersOP += 1
            key.play()
            evaluate()
            operator = "-"
            calculation_input = "0"
        elif keys[pygame.K_j] \
                or (mouse_clicks[0] and ((((button_indexes[0][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[0][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            press_countersOP += 1
            key.play()
            evaluate()
            operator = "x^y"
            calculation_input = "0"

    elif press_countersOP > 0:
        if press_countersOP == 15:
            press_countersOP = -1
        press_countersOP += 1

    if press_countersSOP == 0:
        # X Squared
        if keys[pygame.K_k] \
                or (mouse_clicks[0] and ((((button_indexes[1][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[1][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            operator = "x^2"
            key.play()
            evaluate()
            press_countersSOP += 1
        # Square Root Of x
        if keys[pygame.K_l] \
                or (mouse_clicks[0] and ((((button_indexes[2][1][0] + 50 - mouse_pos[0]) ** 2) +
                                          ((button_indexes[2][1][1] + 50 - mouse_pos[1]) ** 2)) <= 1600)):
            operator = "sqrt(x)"
            key.play()
            evaluate()
            press_countersSOP += 1
    elif press_countersSOP > 0:
        if press_countersSOP == 15:
            press_countersSOP = -1
        press_countersSOP += 1


# Draw Window
def drawwindow():
    win.fill(black)
    win.blit(title, (100, 10))
    pygame.draw.rect(win, dark_dark_grey, (25, 50, 400, 200))
    show_storage()
    show_operator()
    show_input()
    for i in range(20):
        pygame.draw.circle(win, button_colors[i], (button_indexes[i][1][0] + 50, button_indexes[i][1][1] + 50), 40)
        win.blit(button_texts[i], (button_indexes[i][1][0] + 50 - button_texts[i].get_width() / 2,
                                   button_indexes[i][1][1] + 50 - button_texts[i].get_height() / 2))
    win.blit(sqrtimg, button_indexes[2][1])

    pygame.display.update()


# Main Loop
run = True
while run:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    try:
        press()
        drawwindow()
    except OverflowError:
        messagebox.showerror("An Error Occured", "Result too large\nQuiting Calculator")
        run = False
pygame.quit()

# File Name: pong_extra_credit.py
# Author Name: Lindsey Kim
# Date: 10/1/2020
# Course: COSC 1
# Short Description: This creates a version of the game pong on the computer.
#

from cs1lib import *
from random import randint, uniform

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1000
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVEMENT = 8
LEFT_UP = "a"
LEFT_DOWN = "z"
RIGHT_UP = "k"
RIGHT_DOWN = "m"
CENTER_X = WINDOW_WIDTH/2
CENTER_Y = WINDOW_HEIGHT/2
BALL_RADIUS = 10
# x and y coordinates of left paddle
left_paddle_x = 0
left_paddle_y = 0
# x and y coordinates of right paddle
right_paddle_x = WINDOW_WIDTH - PADDLE_WIDTH
right_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT
# sets the ball in the middle of the screen
ball_x = CENTER_X
ball_y = CENTER_Y
# sets the initial velocity to 0 which changes when you press space
velocity_y = 0
velocity_x = 0
a_press = False  # left paddle moves up
z_press = False  # left paddle moves down
k_press = False  # right paddle moves up
m_press = False  # right paddle moves down
q_press = False  # quits the game
space_press = False  # restarts game
collision = False
hit_paddle = False
game_over = False
change_color = False
red = 0
green = 0
blue = 0


def background():
    set_clear_color(0, 0, 0)  # sets background to black
    clear()


def set_red_color():
    set_fill_color(1, 0, 0)


# determines which key is being pressed and sets the boolean to true
def key_down(key):
    global a_press, z_press, k_press, m_press, space_press, q_press
    if key == "a":
        a_press = True
    elif key == "z":
        z_press = True
    elif key == "k":
        k_press = True
    elif key == "m":
        m_press = True
    elif key == " ":
        space_press = True
    elif key == "q":
        q_press = True


# determines which key is being released and sets the boolean to true
def key_up(key):
    global a_press, z_press, k_press, m_press, space_press, q_press
    if key == "a":
        a_press = False
    elif key == "z":
        z_press = False
    elif key == "k":
        k_press = False
    elif key == "m":
        m_press = False
    elif key == " ":
        space_press = False
    elif key == "q":
        q_press = False


# determines if the left paddle is touching the top and bottom walls and can move
def left_paddle_movement():
    global left_paddle_y
    if a_press:
        if PADDLE_MOVEMENT <= left_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
            left_paddle_y = left_paddle_y-PADDLE_MOVEMENT
    elif z_press:
        if 0 <= left_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT - PADDLE_MOVEMENT:
            left_paddle_y = left_paddle_y + PADDLE_MOVEMENT


# determines if the right paddle is touching the top and bottom walls and can move
def right_paddle_movement():
    global right_paddle_y
    if k_press:
        if PADDLE_MOVEMENT <= right_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT:
            right_paddle_y = right_paddle_y - PADDLE_MOVEMENT
    elif m_press:
        if 0 <= right_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT - PADDLE_MOVEMENT:
            right_paddle_y = right_paddle_y + PADDLE_MOVEMENT


# sets the constraints to the original position if the space bar is pressed and sets the ball in motion
def start_game():
    global game_over, ball_x, ball_y, velocity_x, velocity_y, left_paddle_x, left_paddle_y, right_paddle_x, \
        right_paddle_y, space_press
    if space_press:
        game_over = False
        ball_x = CENTER_X
        ball_y = CENTER_Y
        left_paddle_x = 0
        left_paddle_y = 0
        right_paddle_x = WINDOW_WIDTH - PADDLE_WIDTH
        right_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT

        # sets the velocity in the x and y direction as random
        sign_x = randint(0, 1)
        if sign_x == 0:
            velocity_x = randint(3, 7)
        else:
            velocity_x = randint(-7, -3)

        sign_y = randint(0, 1)
        if sign_y == 0:
            velocity_y = randint(3, 7)
        else:
            velocity_y = randint(-7, -3)


# if the ball hits the paddle, it moves it in the opposite direction
def ball_collision_x():
    global ball_x, velocity_x, change_color, red, green, blue

    left_bottom_y = left_paddle_y + PADDLE_HEIGHT
    right_bottom_y = right_paddle_y + PADDLE_HEIGHT

    if ball_x - BALL_RADIUS <= left_paddle_x + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_bottom_y:
        if not game_over:
            velocity_x = -1 * (velocity_x-2)
            ball_x = ball_x + BALL_RADIUS
            red = uniform(0, 1)
            green = uniform(0, 1)
            blue = uniform(0, 1)
            change_color=True

    elif ball_x + BALL_RADIUS >= right_paddle_x and right_paddle_y <= ball_y <= right_bottom_y:
        if not game_over:
            velocity_x = -1 * (velocity_x + 2)
            ball_x = ball_x - BALL_RADIUS
            red = uniform(0, 1)
            green = uniform(0, 1)
            blue = uniform(0, 1)
            change_color=True


# bounces if it hits a horizontal wall and moves
def ball_collision_y():
    global ball_y, velocity_y, ball_x, velocity_x, hit_paddle, collision, game_over, left_paddle_y, right_paddle_y

    if ball_y > WINDOW_HEIGHT - BALL_RADIUS or ball_y < BALL_RADIUS:
        velocity_y = -1 * velocity_y

    if not game_over and not space_press:
        ball_y = ball_y + velocity_y
        ball_x = ball_x + velocity_x


# ends the game if it hits a wall
def game_end():
    global ball_x, ball_y, game_over, velocity_x,velocity_y, space_press, q_press
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WINDOW_WIDTH:
        game_over = True

    if game_over:
        set_fill_color(1, 1, 1)
        draw_rectangle(CENTER_X - 200, CENTER_Y - 50, 400, 100)
        draw_text("Play again?", CENTER_X - 30, CENTER_Y - 10)
        draw_text("Press space to play or 'q' for quit.", CENTER_X - 100, CENTER_Y + 10)

        if q_press:
            cs1_quit()


# draws the ball and paddles
def draw():
    global change_color
    if change_color:
        set_fill_color(red, green, blue)
    draw_circle(ball_x, ball_y, BALL_RADIUS)
    set_red_color()
    draw_rectangle(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(right_paddle_x,right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)


def main():
    global hit_paddle, velocity_x, velocity_y, ball_x, ball_y
    start_game()
    background()
    left_paddle_movement()
    right_paddle_movement()
    ball_collision_x()
    ball_collision_y()
    game_end()
    draw()


start_graphics(main, key_press=key_down, key_release=key_up, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

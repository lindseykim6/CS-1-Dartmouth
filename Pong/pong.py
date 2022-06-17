# File Name: pong.py
# Author Name: Lindsey Kim
# Date: 10/1/2020
# Course: COSC 1
# Short Description: This creates a version of the game pong on the computer.
#

from cs1lib import *


WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1000
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVEMENT = 5
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
ball_x = CENTER_X
ball_y = CENTER_Y
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


def background():
    set_clear_color(0, 0, 0)  # sets background to black
    clear()


def set_red_color():
    set_fill_color(1, 0, 0)


def set_yellow_color():
    set_fill_color(1, 1, 0)


# determines which key is being pressed and sets the boolean to true
def key_down(key):
    global a_press, z_press, k_press, m_press, space_press, n_press, y_press, q_press
    if key == "a":  # left paddle moves up
        a_press = True
    elif key == "z":  # left paddle moves down
        z_press = True
    elif key == "k":  # right paddle moves up
        k_press = True
    elif key == "m":  # right paddle moves down
        m_press = True
    elif key == " ":  # restarts game
        space_press = True
    elif key == "q":  # quits the game
        q_press = True


# determines which key is being released and sets the boolean to true
def key_up(key):
    global a_press, z_press, k_press, m_press, space_press, y_press, n_press, q_press
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
        if PADDLE_MOVEMENT <= left_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT:  # checks if left paddle can go up
            left_paddle_y = left_paddle_y-PADDLE_MOVEMENT
    elif z_press:
        if 0 <= left_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT - PADDLE_MOVEMENT:  # checks if left paddle can go down
            left_paddle_y = left_paddle_y + PADDLE_MOVEMENT


# determines if the right paddle is touching the top and bottom walls and can move
def right_paddle_movement():
    global right_paddle_y
    if k_press:
        if PADDLE_MOVEMENT <= right_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT:  # checks if right paddle can go up
            right_paddle_y = right_paddle_y - PADDLE_MOVEMENT
    elif m_press:
        if 0 <= right_paddle_y <= WINDOW_HEIGHT - PADDLE_HEIGHT - PADDLE_MOVEMENT:  # checks if right paddle can go down
            right_paddle_y = right_paddle_y + PADDLE_MOVEMENT


# sets the constraints to the original position if the space bar is pressed and sets the ball in motion
def start_game():
    global ball_x, ball_y, velocity_x, velocity_y, left_paddle_x, left_paddle_y, right_paddle_x, \
        right_paddle_y

    if space_press:
        ball_x = CENTER_X
        ball_y = CENTER_Y
        left_paddle_x = 0
        left_paddle_y = 0
        right_paddle_x = WINDOW_WIDTH - PADDLE_WIDTH
        right_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT
        velocity_x = 5  # sets the ball in motion in the x direction
        velocity_y = 5  # sets the ball in motion in the y direction


# quits the game if the game is over
def quit_game():
    if q_press:
        cs1_quit()


# if the ball hits the paddle, it moves it in the opposite direction
def ball_collision_paddle():
    global ball_y, velocity_y, ball_x, velocity_x, hit_paddle, collision, left_paddle_y, right_paddle_y, q_press

    left_bottom_y = left_paddle_y + PADDLE_HEIGHT
    right_bottom_y = right_paddle_y + PADDLE_HEIGHT

    # checks if the ball touches the boundaries of the left paddle
    if ball_x - BALL_RADIUS <= left_paddle_x + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_bottom_y:
        velocity_x = -1 * velocity_x
        ball_x = ball_x + BALL_RADIUS
    # checks if the ball touches the boundaries of the right paddle
    elif ball_x + BALL_RADIUS >= right_paddle_x and right_paddle_y <= ball_y <= right_bottom_y:
        velocity_x = -1 * velocity_x
        ball_x = ball_x - BALL_RADIUS


# if the ball hits the wall, it quits
def game_over():
    global q_press, ball_x, ball_y, velocity_y
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WINDOW_WIDTH:
        q_press = True


# bounces if it hits a horizontal wall and moves
def ball_movement():
    global velocity_y, ball_y, ball_x
    if ball_y > WINDOW_HEIGHT - BALL_RADIUS or ball_y < BALL_RADIUS:  # checks if the ball is in the boundaries
        velocity_y = -1 * velocity_y

    ball_y = ball_y + velocity_y  # moves the ball in the y direction by the velocity
    ball_x = ball_x + velocity_x  # moves the ball in the x direction by the velocity


# draws the ball and paddles
def draw():
    global ball_x, ball_y
    set_yellow_color()
    draw_circle(ball_x, ball_y, BALL_RADIUS) # draws the ball
    set_red_color()
    draw_rectangle(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # draws the paddles
    draw_rectangle(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)


def main():
    global hit_paddle, velocity_x, velocity_y, ball_x, ball_y
    start_game()
    background()
    quit_game()
    left_paddle_movement()
    right_paddle_movement()
    ball_collision_paddle()
    ball_movement()
    game_over()
    draw()


start_graphics(main, key_press=key_down, key_release=key_up, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Question
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
#  If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
import math


class Dir:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


def robot(steps):
    y = 0
    x = 0
    for move in steps:
        if move[1] == Dir.UP:
            y += move[0]
        elif move[1] == Dir.DOWN:
            y -= move[0]
        elif move[1] == Dir.LEFT:
            x -= move[0]
        elif move[1] == Dir.RIGHT:
            x += move[0]
    distance = int(math.sqrt(x ** 2 + y ** 2))
    return distance


def test_robot():
    assert robot([(5, Dir.UP), (3, Dir.DOWN), (3, Dir.LEFT), (2, Dir.RIGHT)]) == 2
    assert robot([(100, Dir.UP), (100, Dir.RIGHT), (100, Dir.DOWN), (100, Dir.LEFT)]) == 0
    assert robot([(0, Dir.UP)]) == 0

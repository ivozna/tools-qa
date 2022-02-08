def up(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0] + 1, head[1])
    snake_pos.insert(0, new_head)
    return snake_pos


def down(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0] - 1, head[1])
    snake_pos.insert(0, new_head)
    return snake_pos


def right(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0], head[1] + 1)
    snake_pos.insert(0, new_head)
    return snake_pos


def left(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0], head[1] - 1)
    snake_pos.insert(0, new_head)
    return snake_pos


def snake(board_size, snake_len, steps):
    snake = list(reversed([(0, i) for i in range(0, snake_len)]))
    current = 'right'
    for step in steps:
        current = step or current
        if current == "left":
            snake = left(snake)
        if current == "right":
            snake = right(snake)
        if current == "up":
            snake = up(snake)
        if current == "down":
            snake = down(snake)
    return snake


def test_snake():
    assert snake(8, 2, [0, "up", 0, "right", 0, "up", "left"]) == [(3, 3), (3, 4)]
    assert snake(8, 3, ["right", "right", "right", "up", "up"]) == [(2, 5), (1, 5), (0, 5)]


def test_up():
    assert up([(0, 2), (0, 1), (0, 0)]) == [(1, 2), (0, 2), (0, 1)]
    assert up([(5, 4), (5, 5), (5, 6), (6, 6), (7, 6)]) == [(6, 4), (5, 4), (5, 5), (5, 6), (6, 6)]

import random
import tkinter as tk

CELL = 20
WIDTH, HEIGHT = 30, 20
SPEED = 150

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (1, 0)
food = None
running = False
score = 0


def spawn_food():
    while True:
        pos = (random.randrange(WIDTH), random.randrange(HEIGHT))
        if pos not in snake:
            return pos


def restart():
    global snake, direction, food, score
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (1, 0)
    score = 0
    food = spawn_food()
    score_var.set(f"Score: {score}")
    status_var.set("")
    step()


def step():
    global food, score
    if not running:
        return
    head = (snake[-1][0] + direction[0], snake[-1][1] + direction[1])
    if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT
            or head in snake):
        status_var.set("Game Over! Press R to restart")
        return
    snake.append(head)
    if head == food:
        score += 1
        score_var.set(f"Score: {score}")
        food = spawn_food()
    else:
        snake.pop(0)
    draw()
    win.after(SPEED, step)


def draw():
    canvas.delete("all")
    for x, y in snake:
        canvas.create_rectangle(x * CELL, y * CELL, x * CELL + CELL,
                                y * CELL + CELL, fill="green")
    fx, fy = food
    canvas.create_oval(fx * CELL, fy * CELL, fx * CELL + CELL,
                       fy * CELL + CELL, fill="red")


def key(e):
    global direction, running
    if e.keysym == "Up" and direction != (0, 1):
        direction = (0, -1)
    elif e.keysym == "Down" and direction != (0, -1):
        direction = (0, 1)
    elif e.keysym == "Left" and direction != (1, 0):
        direction = (-1, 0)
    elif e.keysym == "Right" and direction != (-1, 0):
        direction = (1, 0)
    elif e.keysym == "r" or e.keysym == "R":
        restart()
        return
    if not running:
        running = True
        step()


win = tk.Tk()
win.title("Snake")
score_var = tk.StringVar(value="Score: 0")
status_var = tk.StringVar(value="")
tk.Label(win, textvariable=score_var).pack()
tk.Label(win, textvariable=status_var, fg="red").pack()
canvas = tk.Canvas(win, width=WIDTH * CELL, height=HEIGHT * CELL, bg="black")
canvas.pack()
win.bind("<Key>", key)
food = spawn_food()
draw()
win.mainloop()
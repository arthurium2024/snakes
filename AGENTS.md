# AGENTS.md

Single-file tkinter snake game (`snake.py`). No external dependencies — tkinter ships with Python, and `pygame` is deliberately NOT used (not installed). Keep the game dependency-free.

## Run

```
python snake.py
```

Windowed GUI app; blocks on `mainloop()` until the window closes. Arrow keys move, `R` restarts.

## Conventions

- Use tkinter primitives (Canvas `create_rectangle`/`create_oval`) for rendering — don't introduce new libs or assets.
- No tests, linter, or build config exist; verify changes by running the game and playing briefly.
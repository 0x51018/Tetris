# Tetris
A personal Tetris clone project built by hand with minimal AI assistance

## uv usage tutorial for me (trying to not forget)

if there is no .venv folder in local, then do it.
```bash
uv venv --python 3.13
```
then sync to our pyproject.toml and uv.lock with typing next to bash.
```bash
uv sync
```

and use next command to run python file with uv venv.
```bash
uv run ./src/tetris/main.py
```
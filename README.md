# Game Design & Addiction
### Presented at Boston Indies Lightning Talks, 06/18/2024

## Precompiled slides available [here](https://crumblingmizzle.github.io/addfriction/)

## Compilation Instructions
Requirements:

Install manimce + its dependencies (including texlive), then run
```
pipx install "manim-slides[pyqt6-full]"
```

To compile:
```
manim-slides render -qk main.py MainScene
manim-slides convert MainScene index.html
```

To view:
```
firefox index.html
```

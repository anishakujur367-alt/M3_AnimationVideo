
from manim import *

class FirstAnimation(Scene):
    def construct(self):

        title = Text("My First Manim Animation")

        self.play(Write(title))
        self.wait(2)

        self.play(FadeOut(title))

        matrix = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.play(Create(matrix))
        self.wait(3)

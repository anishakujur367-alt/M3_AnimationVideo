
from manim import *

class MatrixAnimation(Scene):
    def construct(self):

        # OPENING TITLE
        title = Text(
            "Understanding Matrices",
            font_size=46,
            color=BLUE
        )

        subtitle = Text(
            "Matrices and Matrix Operations",
            font_size=27
        )
        subtitle.next_to(title, DOWN, buff=0.3)

        student = Text(
            "Presented by: Anisha Kujur | ID: E25B070621",
            font_size=20
        )
        student.next_to(subtitle, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.play(FadeIn(student))
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(student)
        )

        # SCENE 1: IMAGE TO MATRIX
        heading = Text(
            "How does a computer represent an image?",
            font_size=30,
            color=YELLOW
        )
        heading.to_edge(UP)

        self.play(Write(heading))

        # Pixel values of a small image
        values = [
            [1, 3, 5],
            [2, 7, 6],
            [0, 4, 9]
        ]

        pixels = VGroup()

        for i in range(3):
            for j in range(3):

                value = values[i][j]

                square = Square(
                    side_length=0.65
                )
                square.set_fill(
                    interpolate_color(BLACK, BLUE, value / 9),
                    opacity=1
                )
                square.set_stroke(WHITE, width=1)

                number = Text(
                    str(value),
                    font_size=22
                )
                number.move_to(square.get_center())

                cell = VGroup(square, number)
                cell.move_to(
                    LEFT * 4
                    + RIGHT * j * 0.7
                    + DOWN * i * 0.7
                )

                pixels.add(cell)

        pixel_label = Text(
            "Pixel values",
            font_size=24
        )
        pixel_label.next_to(pixels, DOWN, buff=0.4)

        self.play(
            LaggedStart(
                *[FadeIn(pixel) for pixel in pixels],
                lag_ratio=0.15
            )
        )
        self.play(FadeIn(pixel_label))

        # Arrow
        arrow = Arrow(
            LEFT * 1.5,
            RIGHT * 0.5,
            color=YELLOW
        )

        self.play(GrowArrow(arrow))

        # Matrix representation
        matrix = Matrix(values)
        matrix.scale(0.9)
        matrix.move_to(RIGHT * 3)

        matrix_label = Text(
            "A matrix",
            font_size=24
        )
        matrix_label.next_to(matrix, DOWN, buff=0.4)

        self.play(Write(matrix))
        self.play(FadeIn(matrix_label))

        explanation = Text(
            "A matrix organises numbers into rows and columns.",
            font_size=23,
            color=GREEN
        )
        explanation.to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(3)

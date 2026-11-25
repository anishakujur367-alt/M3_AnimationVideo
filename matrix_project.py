from manim import *


class MatrixAnimation(Scene):
    def construct(self):

        # =====================================
        # OPENING TITLE
        # =====================================

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

        # =====================================
        # SCENE 1: IMAGE TO MATRIX
        # =====================================

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

        # Arrow connecting pixels to matrix
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

        # Clear Scene 1
        self.play(
            FadeOut(heading),
            FadeOut(pixels),
            FadeOut(pixel_label),
            FadeOut(arrow),
            FadeOut(matrix),
            FadeOut(matrix_label),
            FadeOut(explanation)
        )

        # =====================================
        # SCENE 2: MATRIX DIMENSIONS
        # =====================================

        heading2 = Text(
            "Understanding Matrix Dimensions",
            font_size=34,
            color=YELLOW
        )
        heading2.to_edge(UP)

        self.play(Write(heading2))

        # Define a 2 x 2 matrix
        A = Matrix([
            [2, 4],
            [6, 8]
        ])

        A.scale(1.2)
        A.shift(LEFT * 2)

        self.play(Write(A))

        # Explain matrix dimensions
        dimension = MathTex(
            r"\text{Dimension} = 2 \times 2",
            color=GREEN
        )

        dimension.scale(0.9)
        dimension.next_to(A, DOWN, buff=0.7)

        self.play(Write(dimension))

        # Explain rows
        rows_text = Text(
            "2 Rows",
            font_size=27,
            color=BLUE
        )
        rows_text.next_to(A, UP, buff=0.5)

        # Explain columns
        columns_text = Text(
            "2 Columns",
            font_size=27,
            color=GREEN
        )
        columns_text.next_to(A, RIGHT, buff=1)

        self.play(FadeIn(rows_text))
        self.play(FadeIn(columns_text))
        self.wait(2)

        # =====================================
        # SCENE 2: INDIVIDUAL MATRIX ENTRIES
        # =====================================

        entry_heading = Text(
            "Understanding Individual Entries",
            font_size=27,
            color=YELLOW
        )
        entry_heading.to_edge(UP)

        self.play(
            FadeOut(heading2),
            FadeOut(rows_text),
            FadeOut(columns_text),
            FadeOut(dimension),
            FadeIn(entry_heading)
        )

        # Entry notation
        entry = MathTex(
            r"a_{ij}",
            color=YELLOW
        )

        entry.scale(1.5)
        entry.move_to(RIGHT * 3 + UP * 0.8)

        # Explain subscripts
        meaning = VGroup(
            MathTex(r"i = \text{Row number}"),
            MathTex(r"j = \text{Column number}")
        )

        meaning.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.5
        )

        meaning.scale(0.8)
        meaning.next_to(entry, DOWN, buff=0.5)

        self.play(Write(entry))
        self.play(FadeIn(meaning))

        # =====================================
        # HIGHLIGHT ENTRIES WITH MATCHING EQUATIONS
        # =====================================

        entries = A.get_entries()

        entry_labels = [
            MathTex(r"a_{11}=2", color=GREEN),
            MathTex(r"a_{12}=4", color=GREEN),
            MathTex(r"a_{21}=6", color=GREEN),
            MathTex(r"a_{22}=8", color=GREEN)
        ]

        # Keep all equations at the same screen position
        for label in entry_labels:
            label.scale(1.2)
            label.to_edge(DOWN)

        # First entry: a11 = 2
        highlight = SurroundingRectangle(
            entries[0],
            color=RED,
            buff=0.15
        )

        current_label = entry_labels[0]

        self.play(
            Create(highlight),
            Write(current_label)
        )

        self.wait(1.5)

        # Remaining entries
        for i in range(1, 4):

            new_highlight = SurroundingRectangle(
                entries[i],
                color=RED,
                buff=0.15
            )

            new_label = entry_labels[i]

            self.play(
                Transform(highlight, new_highlight),
                Transform(current_label, new_label)
            )

            self.wait(1.5)

        self.wait(2)

        # Clear Scene 2
        self.play(
            FadeOut(A),
            FadeOut(highlight),
            FadeOut(entry_heading),
            FadeOut(entry),
            FadeOut(meaning),
            FadeOut(current_label)
        )

        self.wait(1)

        # =====================================
        # SCENE 3: VISUAL INTUITION OF OPERATIONS
        # =====================================

        heading3 = Text(
            "Understanding Matrix Operations",
            font_size=32,
            color=YELLOW
        )
        heading3.to_edge(UP)

        self.play(Write(heading3))

        # Two matrices for our examples
        matrix_A = Matrix([
            [1, 2],
            [3, 4]
        ])

        matrix_B = Matrix([
            [5, 6],
            [7, 8]
        ])

        matrix_A.scale(1.1)
        matrix_B.scale(1.1)

        matrix_A.move_to(LEFT * 2.5)
        matrix_B.move_to(RIGHT * 2.5)

        label_A = MathTex("A")
        label_B = MathTex("B")

        label_A.next_to(matrix_A, UP, buff=0.4)
        label_B.next_to(matrix_B, UP, buff=0.4)

        self.play(
            Write(matrix_A),
            Write(matrix_B)
        )

        self.play(
            FadeIn(label_A),
            FadeIn(label_B)
        )

        self.wait(2)

        # -------------------------------------
        # 1. MATRIX ADDITION INTRODUCTION
        # -------------------------------------

        plus_sign = MathTex("+")
        plus_sign.scale(1.3)
        plus_sign.move_to(ORIGIN)

        addition_text = Text(
            "1. Matrix Addition",
            font_size=27,
            color=GREEN
        )
        addition_text.to_edge(DOWN)

        addition_note = Text(
            "Add the entries in the same position",
            font_size=24
        )
        addition_note.next_to(addition_text, UP, buff=0.3)

        self.play(
            Write(addition_text),
            FadeIn(plus_sign)
        )

        # Highlight corresponding first entries
        highlight_A = SurroundingRectangle(
            matrix_A.get_entries()[0],
            color=RED,
            buff=0.12
        )

        highlight_B = SurroundingRectangle(
            matrix_B.get_entries()[0],
            color=RED,
            buff=0.12
        )

        self.play(
            Create(highlight_A),
            Create(highlight_B)
        )

        self.play(Write(addition_note))
        self.wait(2)

        # Remove everything that belongs to addition
        self.play(
            FadeOut(highlight_A),
            FadeOut(highlight_B),
            FadeOut(addition_text),
            FadeOut(addition_note),
            FadeOut(plus_sign)
        )

        # -------------------------------------
        # 2. SCALAR MULTIPLICATION INTRODUCTION
        # -------------------------------------

        # First remove A and B so nothing overlaps
        self.play(
            FadeOut(matrix_A),
            FadeOut(matrix_B),
            FadeOut(label_A),
            FadeOut(label_B)
        )

        scalar_text = Text(
            "2. Scalar Multiplication",
            font_size=27,
            color=GREEN
        )
        scalar_text.to_edge(DOWN)

        scalar_note = Text(
            "Multiply every entry by the same number",
            font_size=24
        )
        scalar_note.next_to(scalar_text, UP, buff=0.3)

        scalar_equation = MathTex(
            r"2A = 2\begin{bmatrix}1&2\\3&4\end{bmatrix}"
        )
        scalar_equation.scale(1.0)
        scalar_equation.move_to(ORIGIN)

        self.play(Write(scalar_text))
        self.play(Write(scalar_equation))
        self.play(Write(scalar_note))
        self.wait(3)

        self.play(
            FadeOut(scalar_equation),
            FadeOut(scalar_note),
            FadeOut(scalar_text)
        )

        # -------------------------------------
        # 3. MATRIX MULTIPLICATION INTRODUCTION
        # -------------------------------------

        # Bring A and B back
        self.play(
            FadeIn(matrix_A),
            FadeIn(matrix_B),
            FadeIn(label_A),
            FadeIn(label_B)
        )

        times_sign = MathTex(r"\times")
        times_sign.scale(1.3)
        times_sign.move_to(ORIGIN)

        multiplication_text = Text(
            "3. Matrix Multiplication",
            font_size=27,
            color=GREEN
        )
        multiplication_text.to_edge(DOWN)

        self.play(
            Write(multiplication_text),
            FadeIn(times_sign)
        )

        # Highlight first row of Matrix A
        row_highlight = SurroundingRectangle(
            matrix_A.get_rows()[0],
            color=RED,
            buff=0.12
        )

        # Highlight first column of Matrix B
        column_highlight = SurroundingRectangle(
            VGroup(
                matrix_B.get_entries()[0],
                matrix_B.get_entries()[2]
            ),
            color=BLUE,
            buff=0.12
        )

        self.play(Create(row_highlight))
        self.wait(1.5)

        self.play(Create(column_highlight))
        self.wait(2)

        row_column_text = Text(
            "Multiply a row by a column",
            font_size=25,
            color=YELLOW
        )
        row_column_text.to_edge(DOWN)

        self.play(
            FadeOut(multiplication_text),
            Write(row_column_text)
        )

        self.wait(3)

        # Clear Scene 3
        self.play(
            FadeOut(heading3),
            FadeOut(matrix_A),
            FadeOut(matrix_B),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(times_sign),
            FadeOut(row_highlight),
            FadeOut(column_highlight),
            FadeOut(row_column_text)
        )

        self.wait(1)
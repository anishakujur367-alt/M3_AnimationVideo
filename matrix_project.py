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

        # =====================================
        # SCENE 4: WORKED EXAMPLES
        # =====================================

        # -------------------------------------
        # EXAMPLE 1: MATRIX ADDITION
        # -------------------------------------

        heading4a = Text(
            "Worked Example 1: Matrix Addition",
            font_size=32,
            color=YELLOW
        )
        heading4a.to_edge(UP)

        self.play(Write(heading4a))

        add_A = Matrix([[1, 2], [3, 4]])
        add_B = Matrix([[5, 6], [7, 8]])
        add_R = Matrix([[6, 8], [10, 12]])

        add_A.scale(0.9)
        add_B.scale(0.9)
        add_R.scale(0.9)

        add_plus = MathTex("+")
        add_equals = MathTex("=")

        # Put everything in one row
        add_row = VGroup(add_A, add_plus, add_B, add_equals, add_R)
        add_row.arrange(RIGHT, buff=0.45)
        add_row.move_to(UP * 0.6)

        add_label_A = MathTex("A").next_to(add_A, UP, buff=0.3)
        add_label_B = MathTex("B").next_to(add_B, UP, buff=0.3)
        add_label_R = MathTex("A + B").next_to(add_R, UP, buff=0.3)
        add_labels = VGroup(add_label_A, add_label_B, add_label_R)

        # Show A, B and only the empty brackets of the answer
        self.play(
            FadeIn(add_A),
            FadeIn(add_plus),
            FadeIn(add_B),
            FadeIn(add_equals),
            FadeIn(add_R.get_brackets()),
            FadeIn(add_labels)
        )

        self.wait(1)

        add_calcs = [
            r"1 + 5 = 6",
            r"2 + 6 = 8",
            r"3 + 7 = 10",
            r"4 + 8 = 12"
        ]

        for k in range(4):

            hl_A = SurroundingRectangle(
                add_A.get_entries()[k],
                color=RED,
                buff=0.12
            )
            hl_B = SurroundingRectangle(
                add_B.get_entries()[k],
                color=RED,
                buff=0.12
            )

            calc = MathTex(add_calcs[k], color=YELLOW)
            calc.scale(1.2)
            calc.move_to(DOWN * 1.8)

            result_entry = add_R.get_entries()[k]
            result_entry.set_color(GREEN)

            self.play(Create(hl_A), Create(hl_B))
            self.play(Write(calc))
            self.play(Write(result_entry))
            self.wait(1)
            self.play(
                FadeOut(hl_A),
                FadeOut(hl_B),
                FadeOut(calc)
            )

        add_note = Text(
            "Addition needs matrices of the same dimensions",
            font_size=24,
            color=GREEN
        )
        add_note.to_edge(DOWN)

        self.play(Write(add_note))
        self.wait(2)

        # Clear Example 1
        self.play(
            FadeOut(heading4a),
            FadeOut(add_row),
            FadeOut(add_labels),
            FadeOut(add_note)
        )

        # -------------------------------------
        # EXAMPLE 2: SCALAR MULTIPLICATION
        # -------------------------------------

        heading4b = Text(
            "Worked Example 2: Scalar Multiplication",
            font_size=32,
            color=YELLOW
        )
        heading4b.to_edge(UP)

        self.play(Write(heading4b))

        sc_two = MathTex("2")
        sc_two.scale(1.3)

        sc_A = Matrix([[1, 2], [3, 4]])
        sc_R = Matrix([[2, 4], [6, 8]])

        sc_A.scale(0.9)
        sc_R.scale(0.9)

        sc_equals = MathTex("=")

        sc_row = VGroup(sc_two, sc_A, sc_equals, sc_R)
        sc_row.arrange(RIGHT, buff=0.5)
        sc_row.move_to(UP * 0.6)

        sc_label_A = MathTex("A").next_to(sc_A, UP, buff=0.3)
        sc_label_R = MathTex("2A").next_to(sc_R, UP, buff=0.3)
        sc_labels = VGroup(sc_label_A, sc_label_R)

        self.play(
            FadeIn(sc_two),
            FadeIn(sc_A),
            FadeIn(sc_equals),
            FadeIn(sc_R.get_brackets()),
            FadeIn(sc_labels)
        )

        # Blue box on the scalar: the same number is used every time
        sc_two_box = SurroundingRectangle(
            sc_two,
            color=BLUE,
            buff=0.15
        )
        self.play(Create(sc_two_box))
        self.wait(1)

        sc_calcs = [
            r"2 \times 1 = 2",
            r"2 \times 2 = 4",
            r"2 \times 3 = 6",
            r"2 \times 4 = 8"
        ]

        for k in range(4):

            hl = SurroundingRectangle(
                sc_A.get_entries()[k],
                color=RED,
                buff=0.12
            )

            calc = MathTex(sc_calcs[k], color=YELLOW)
            calc.scale(1.2)
            calc.move_to(DOWN * 1.8)

            result_entry = sc_R.get_entries()[k]
            result_entry.set_color(GREEN)

            self.play(Create(hl))
            self.play(Write(calc))
            self.play(Write(result_entry))
            self.wait(1)
            self.play(
                FadeOut(hl),
                FadeOut(calc)
            )

        sc_note = Text(
            "The scalar 2 multiplies every entry",
            font_size=24,
            color=GREEN
        )
        sc_note.to_edge(DOWN)

        self.play(Write(sc_note))
        self.wait(2)

        # Clear Example 2
        self.play(
            FadeOut(heading4b),
            FadeOut(sc_row),
            FadeOut(sc_labels),
            FadeOut(sc_two_box),
            FadeOut(sc_note)
        )

        # -------------------------------------
        # EXAMPLE 3: MATRIX MULTIPLICATION
        # -------------------------------------

        heading4c = Text(
            "Worked Example 3: Matrix Multiplication",
            font_size=32,
            color=YELLOW
        )
        heading4c.to_edge(UP)

        self.play(Write(heading4c))

        mu_A = Matrix([[1, 2], [3, 4]])
        mu_B = Matrix([[5, 6], [7, 8]])
        mu_R = Matrix([[19, 22], [43, 50]])

        mu_A.scale(0.9)
        mu_B.scale(0.9)
        mu_R.scale(0.9)

        mu_times = MathTex(r"\times")
        mu_equals = MathTex("=")

        mu_row = VGroup(mu_A, mu_times, mu_B, mu_equals, mu_R)
        mu_row.arrange(RIGHT, buff=0.45)
        mu_row.move_to(UP * 0.6)

        mu_label_A = MathTex("A").next_to(mu_A, UP, buff=0.3)
        mu_label_B = MathTex("B").next_to(mu_B, UP, buff=0.3)
        mu_label_R = MathTex("AB").next_to(mu_R, UP, buff=0.3)
        mu_labels = VGroup(mu_label_A, mu_label_B, mu_label_R)

        self.play(
            FadeIn(mu_A),
            FadeIn(mu_times),
            FadeIn(mu_B),
            FadeIn(mu_equals),
            FadeIn(mu_R.get_brackets()),
            FadeIn(mu_labels)
        )

        self.wait(1)

        mu_calcs = [
            r"1 \times 5 + 2 \times 7 = 19",
            r"1 \times 6 + 2 \times 8 = 22",
            r"3 \times 5 + 4 \times 7 = 43",
            r"3 \times 6 + 4 \times 8 = 50"
        ]

        ent_A = mu_A.get_entries()
        ent_B = mu_B.get_entries()

        for k in range(4):

            r = k // 2   # which row of A
            c = k % 2    # which column of B

            row_hl = SurroundingRectangle(
                VGroup(ent_A[2 * r], ent_A[2 * r + 1]),
                color=RED,
                buff=0.12
            )

            col_hl = SurroundingRectangle(
                VGroup(ent_B[c], ent_B[c + 2]),
                color=BLUE,
                buff=0.12
            )

            calc = MathTex(mu_calcs[k], color=YELLOW)
            calc.scale(1.1)
            calc.move_to(DOWN * 1.8)

            result_entry = mu_R.get_entries()[k]
            result_entry.set_color(GREEN)

            self.play(Create(row_hl), Create(col_hl))
            self.play(Write(calc))
            self.play(Write(result_entry))
            self.wait(1.5)
            self.play(
                FadeOut(row_hl),
                FadeOut(col_hl),
                FadeOut(calc)
            )

        # Dimension rule
        dim_rule = MathTex(
            r"(2 \times 2)(2 \times 2) = (2 \times 2)",
            color=YELLOW
        )
        dim_rule.move_to(DOWN * 1.8)

        dim_note = Text(
            "The inner numbers must match. The outer numbers give the size.",
            font_size=24,
            color=GREEN
        )
        dim_note.to_edge(DOWN)

        self.play(Write(dim_rule))
        self.play(Write(dim_note))
        self.wait(3)

        # Clear Example 3
        self.play(
            FadeOut(heading4c),
            FadeOut(mu_row),
            FadeOut(mu_labels),
            FadeOut(dim_rule),
            FadeOut(dim_note)
        )

        self.wait(1)

        # =====================================
        # SCENE 5: INTERPRETATION AND APPLICATIONS
        # =====================================

        # -------------------------------------
        # PART 1: WHY THE INNER NUMBERS MUST MATCH
        # -------------------------------------

        heading5a = Text(
            "Understanding Matrix Multiplication",
            font_size=32,
            color=YELLOW
        )
        heading5a.to_edge(UP)

        self.play(Write(heading5a))

        # A 2x3 matrix times a 3x2 matrix
        mat_P = Matrix([[1, 2, 3], [4, 5, 6]])
        mat_Q = Matrix([[7, 8], [9, 10], [11, 12]])
        mat_R = Matrix([[58, 64], [139, 154]])

        mat_P.scale(0.8)
        mat_Q.scale(0.8)
        mat_R.scale(0.8)

        dim_times = MathTex(r"\times")
        dim_equals = MathTex("=")

        dim_row = VGroup(mat_P, dim_times, mat_Q, dim_equals, mat_R)
        dim_row.arrange(RIGHT, buff=0.45)
        dim_row.move_to(UP * 0.9)

        lab_P = MathTex("P").next_to(mat_P, UP, buff=0.3)
        lab_Q = MathTex("Q").next_to(mat_Q, UP, buff=0.3)
        lab_R = MathTex("PQ").next_to(mat_R, UP, buff=0.3)
        dim_labels = VGroup(lab_P, lab_Q, lab_R)

        # Dimensions under each matrix
        # Inner numbers are yellow, outer numbers are green
        size_P = MathTex("2", r"\times", "3")
        size_P[0].set_color(GREEN)
        size_P[2].set_color(YELLOW)
        size_P.next_to(mat_P, DOWN, buff=0.3)

        size_Q = MathTex("3", r"\times", "2")
        size_Q[0].set_color(YELLOW)
        size_Q[2].set_color(GREEN)
        size_Q.next_to(mat_Q, DOWN, buff=0.3)

        size_R = MathTex("2", r"\times", "2", color=GREEN)
        size_R.next_to(mat_R, DOWN, buff=0.3)

        dim_sizes = VGroup(size_P, size_Q, size_R)

        self.play(
            FadeIn(mat_P),
            FadeIn(dim_times),
            FadeIn(mat_Q),
            FadeIn(dim_equals),
            FadeIn(mat_R.get_brackets()),
            FadeIn(dim_labels)
        )

        self.play(Write(dim_sizes))
        self.wait(1)

        step_text1 = Text(
            "Columns of P = rows of Q: 3 = 3. So we can multiply.",
            font_size=26,
            color=YELLOW
        )
        step_text1.to_edge(DOWN)

        self.play(Write(step_text1))
        self.wait(2)

        # Row 1 of P and column 1 of Q
        ent_P = mat_P.get_entries()
        ent_Q = mat_Q.get_entries()
        ent_R = mat_R.get_entries()

        row_hl_p = SurroundingRectangle(
            VGroup(ent_P[0], ent_P[1], ent_P[2]),
            color=RED,
            buff=0.12
        )

        col_hl_q = SurroundingRectangle(
            VGroup(ent_Q[0], ent_Q[2], ent_Q[4]),
            color=BLUE,
            buff=0.12
        )

        step_text2 = Text(
            "Row 1 has 3 numbers. Column 1 has 3 numbers. They pair up one by one.",
            font_size=24,
            color=YELLOW
        )
        step_text2.to_edge(DOWN)

        self.play(
            Create(row_hl_p),
            Create(col_hl_q),
            FadeOut(step_text1)
        )
        self.play(Write(step_text2))

        big_calc = MathTex(
            r"1 \times 7 + 2 \times 9 + 3 \times 11 = 58",
            color=YELLOW
        )
        big_calc.move_to(DOWN * 1.7)

        ent_R[0].set_color(GREEN)

        self.play(Write(big_calc))
        self.play(Write(ent_R[0]))
        self.wait(2)

        self.play(
            FadeOut(row_hl_p),
            FadeOut(col_hl_q),
            FadeOut(big_calc),
            FadeOut(step_text2)
        )

        # The other three entries
        step_text3 = Text(
            "The same steps fill in the other three entries.",
            font_size=26,
            color=YELLOW
        )
        step_text3.to_edge(DOWN)

        for k in range(1, 4):
            ent_R[k].set_color(GREEN)

        self.play(Write(step_text3))
        self.play(
            LaggedStart(
                *[Write(ent_R[k]) for k in range(1, 4)],
                lag_ratio=0.6
            )
        )
        self.wait(2)

        # Outer numbers give the size of the answer
        step_text4 = Text(
            "Outer numbers: 2 and 2. They give the size of the answer.",
            font_size=26,
            color=GREEN
        )
        step_text4.to_edge(DOWN)

        self.play(
            FadeOut(step_text3),
            Write(step_text4)
        )
        self.wait(3)

        # Clear Part 1
        self.play(
            FadeOut(heading5a),
            FadeOut(dim_row),
            FadeOut(dim_labels),
            FadeOut(dim_sizes),
            FadeOut(step_text4)
        )

        # -------------------------------------
        # PART 2: WHAT EACH OPERATION MEANS
        # -------------------------------------

        heading5b = Text(
            "What do the operations mean?",
            font_size=32,
            color=YELLOW
        )
        heading5b.to_edge(UP)

        self.play(Write(heading5b))

        meaning_lines = VGroup(
            Text(
                "Addition: combines matching entries",
                font_size=26,
                t2c={"Addition": BLUE}
            ),
            Text(
                "Scalar multiplication: changes every entry by the same factor",
                font_size=26,
                t2c={"Scalar multiplication": GREEN}
            ),
            Text(
                "Matrix multiplication: combines rows with columns",
                font_size=26,
                t2c={"Matrix multiplication": RED}
            )
        )

        meaning_lines.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.7
        )
        meaning_lines.move_to(ORIGIN)

        for line in meaning_lines:
            self.play(Write(line))
            self.wait(2)

        self.wait(1)

        self.play(
            FadeOut(heading5b),
            FadeOut(meaning_lines)
        )

        # -------------------------------------
        # PART 3: REAL-LIFE APPLICATIONS
        # -------------------------------------

        heading5c = Text(
            "Where are matrices used?",
            font_size=32,
            color=YELLOW
        )
        heading5c.to_edge(UP)

        self.play(Write(heading5c))

        app_data = [
            ("Computer Graphics", "Rotate and scale\nshapes on screen", BLUE),
            ("Image Processing", "Filters change\npixel values", GREEN),
            ("Machine Learning", "Data and weights are\nstored as matrices", ORANGE)
        ]

        cards = VGroup()

        for name, desc, col in app_data:

            box = RoundedRectangle(
                corner_radius=0.2,
                width=3.7,
                height=2.4,
                color=col
            )

            card_title = Text(name, font_size=26, color=col)
            card_desc = Text(desc, font_size=22)

            card_text = VGroup(card_title, card_desc)
            card_text.arrange(DOWN, buff=0.35)
            card_text.move_to(box.get_center())

            cards.add(VGroup(box, card_text))

        cards.arrange(RIGHT, buff=0.4)
        cards.move_to(ORIGIN)

        self.play(
            LaggedStart(
                *[FadeIn(card) for card in cards],
                lag_ratio=0.5
            )
        )

        apps_note = Text(
            "All of them use the operations you just learned.",
            font_size=24,
            color=GREEN
        )
        apps_note.to_edge(DOWN)

        self.play(Write(apps_note))
        self.wait(4)

        # Clear Scene 5
        self.play(
            FadeOut(heading5c),
            FadeOut(cards),
            FadeOut(apps_note)
        )

        self.wait(1)

        # =====================================
        # SCENE 6: SUMMARY AND CREDITS
        # (the code is in the method scene_six below)
        # =====================================

        self.scene_six()

    def scene_six(self):

        # -------------------------------------
        # SCREEN 1: THREE KEY TAKEAWAYS
        # -------------------------------------

        heading6a = Text(
            "3 Key Takeaways",
            font_size=34,
            color=YELLOW
        )
        heading6a.to_edge(UP)

        self.play(Write(heading6a))

        # Takeaway 1: what a matrix is, its size and its entries
        take1 = VGroup(
            Text(
                "A matrix is a rectangular arrangement of numbers.",
                font_size=24
            ),
            VGroup(
                MathTex(
                    r"\text{size} = \text{rows} \times \text{columns}",
                    font_size=30,
                    color=YELLOW
                ),
                MathTex(
                    r"a_{ij} = \text{entry in row } i,\ \text{column } j",
                    font_size=30,
                    color=YELLOW
                )
            ).arrange(RIGHT, buff=0.8)
        )
        take1.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Takeaway 2: addition and scalar multiplication
        take2 = VGroup(
            Text(
                "Addition and scalar multiplication work entry by entry.",
                font_size=24
            ),
            Text(
                "Addition requires matrices of the same dimensions.",
                font_size=24
            )
        )
        take2.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Takeaway 3: matrix multiplication and the dimension rule
        take3 = VGroup(
            Text(
                "Matrix multiplication is row by column.",
                font_size=24
            ),
            Text(
                "The columns of the first matrix must equal the rows of the second:",
                font_size=24
            ),
            MathTex(
                r"(m \times n)(n \times p) = (m \times p)",
                font_size=30,
                color=YELLOW
            )
        )
        take3.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Stack the three takeaways on the left edge
        takeaways = VGroup(take1, take2, take3)
        takeaways.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        takeaways.move_to(DOWN * 0.2 + RIGHT * 0.5)

        # A numbered circle beside each takeaway
        badge_colors = [BLUE, GREEN, ORANGE]
        take_items = VGroup()

        for n, block in enumerate([take1, take2, take3]):

            circle = Circle(radius=0.28, color=badge_colors[n])

            number_text = Text(
                str(n + 1),
                font_size=24,
                color=badge_colors[n]
            )
            number_text.move_to(circle.get_center())

            badge = VGroup(circle, number_text)
            badge.next_to(block, LEFT, buff=0.4)
            badge.align_to(block, UP)

            take_items.add(VGroup(badge, block))

        # Safety: shrink if the group is ever too tall or too wide
        if take_items.height > 5.6:
            take_items.scale_to_fit_height(5.6)
        if take_items.width > 12.5:
            take_items.scale_to_fit_width(12.5)

        take_waits = [4.5, 3.5, 5]

        for n in range(3):
            self.play(FadeIn(take_items[n], shift=RIGHT * 0.3))
            self.wait(take_waits[n])

        self.wait(2)

        self.play(
            FadeOut(heading6a),
            FadeOut(take_items)
        )

        # -------------------------------------
        # SCREEN 2: CREDITS
        # -------------------------------------

        heading6b = Text(
            "Credits",
            font_size=34,
            color=YELLOW
        )
        heading6b.to_edge(UP)

        self.play(Write(heading6b))

        references_lines = [
            "No external references used.",
            "Mathematical content was reviewed by the student."
        ]

        music_lines = [
            "No background music used."
        ]

        ai_lines = [
            "Claude (Anthropic) and ChatGPT (OpenAI) assisted with project planning,",
            "mathematical explanations, Manim coding, troubleshooting, and script",
            "preparation. The student reviewed the mathematical content and",
            "final animations."
        ]

        credit_data = [
            ("References", GREEN, references_lines),
            ("Music", BLUE, music_lines),
            ("AI Disclosure", ORANGE, ai_lines)
        ]

        credit_sections = VGroup()

        for sec_title, sec_color, sec_lines in credit_data:

            sec_head = Text(
                sec_title,
                font_size=26,
                color=sec_color
            )

            sec_body = VGroup(
                *[Text(line, font_size=21) for line in sec_lines]
            )
            sec_body.arrange(DOWN, aligned_edge=LEFT, buff=0.1)

            section = VGroup(sec_head, sec_body)
            section.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

            credit_sections.add(section)

        credit_sections.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        credit_sections.move_to(DOWN * 0.3)

        # Safety: shrink if the credits are ever too tall or too wide
        if credit_sections.height > 5.4:
            credit_sections.scale_to_fit_height(5.4)
        if credit_sections.width > 12.5:
            credit_sections.scale_to_fit_width(12.5)

        credit_waits = [2.5, 2.5, 8]

        for n in range(3):
            self.play(FadeIn(credit_sections[n], shift=UP * 0.2))
            self.wait(credit_waits[n])

        self.wait(1.5)

        self.play(
            FadeOut(heading6b),
            FadeOut(credit_sections)
        )

        # -------------------------------------
        # SCREEN 3: CLOSING FRAME
        # -------------------------------------

        title6 = Text(
            "Matrices and Matrix Operations",
            font_size=46,
            color=BLUE
        )

        subtitle6 = Text(
            "Thank You for Watching",
            font_size=27
        )
        subtitle6.next_to(title6, DOWN, buff=0.3)

        student6 = Text(
            "Presented by: Anisha Kujur | ID: E25B070621",
            font_size=20
        )
        student6.next_to(subtitle6, DOWN, buff=0.5)

        self.play(Write(title6))
        self.play(FadeIn(subtitle6))
        self.play(FadeIn(student6))
        self.wait(3.5)

        self.play(
            FadeOut(title6),
            FadeOut(subtitle6),
            FadeOut(student6)
        )

        self.wait(1)


class Scene6Preview(MatrixAnimation):
    """Preview helper: plays only Scene 6 so it renders in seconds."""

    def construct(self):
        self.scene_six()
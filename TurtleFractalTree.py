import turtle

# Funktion zum Zeichnen eines Fraktalbaums
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        # Zeichne den Hauptast
        t.forward(branch_length)

        # Rechter Ast
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)

        # Zurück zum Hauptstamm
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)

        # Zurück zur Basis
        t.right(20)
        t.backward(branch_length)

# Hauptfunktion
def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Setze die Zeichengeschwindigkeit

    # Positioniere den Turtle
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Zeichne den Fraktalbaum
    draw_fractal_tree(100, t)

    # Beende das Zeichnen
    screen.exitonclick()

if __name__ == "__main__":
    main()

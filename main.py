import tkinter as tk
import turtle
import math

#L-SYSTEM ENGINE

def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current


#TURTLE RENDERER

def draw_lsystem(t, instructions, angle):
    stack = []
    length = len(instructions)

    turtle.tracer(0, 0)

    for i, cmd in enumerate(instructions):
        # Gradient effect
        t.pencolor(i / length, 0.8, 1 - i / length)

        if cmd == "F":
            t.forward(5)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            stack.append((t.position(), t.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

    turtle.update()


#GUI CALLBACK

def generate():
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    axiom = axiom_entry.get()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())

    #Parse rules
    rules = {}
    rule_text = rule_entry.get().split(",")
    for rule in rule_text:
        key, value = rule.split(":")
        rules[key.strip()] = value.strip()

    final_string = expand_lsystem(axiom, rules, iterations)
    draw_lsystem(t, final_string, angle)


#TKINTER

root = tk.Tk()
root.title("L-System Fractal Architect")

#Canvas for Turtle
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.LEFT)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)
turtle.colormode(1.0)


#Control Panel
panel = tk.Frame(root, padx=10)
panel.pack(side=tk.RIGHT, fill=tk.Y)

tk.Label(panel, text="Axiom").pack()
axiom_entry = tk.Entry(panel)
axiom_entry.insert(0, "F")
axiom_entry.pack()

tk.Label(panel, text="Rules").pack()
rule_entry = tk.Entry(panel, width=30)
rule_entry.insert(0, "F:F[+F]F[-F]F")
rule_entry.pack()

tk.Label(panel, text="Angle").pack()
angle_entry = tk.Entry(panel)
angle_entry.insert(0, "25")
angle_entry.pack()

tk.Label(panel, text="Iterations").pack()
iter_entry = tk.Entry(panel)
iter_entry.insert(0, "4")
iter_entry.pack()

tk.Button(panel, text="Generate", command=generate).pack(pady=10)

root.mainloop()
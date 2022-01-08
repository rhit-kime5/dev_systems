import turtle

class LSystem:

    def __init__(self, axiom, rules, iterations, rotateAngle, distanceUnit):
        self.axiom = axiom
        self.rules = rules
        self.iterations = iterations
        self.rotateAngle = rotateAngle
        self.distanceUnit = distanceUnit

    def generateOnce(self):
        output = ""

        for char in self.axiom:
            if char in self.rules:
                output += self.rules[char]
            else:
                output += char

        self.axiom = output
        return output

    def generate(self, printOn):
        for i in range(self.iterations):
            currAxiom = self.generateOnce()

            if (printOn):
                print("Iteration " + str(i + 1) + ": " + currAxiom)
            
        return self.axiom

    def draw(self):

        branchStack = []
        turtle.left(90)
        
        turtle.tracer(0, 0)

        for char in self.axiom:
            if char == 'F':
                turtle.forward(self.distanceUnit)
            elif char == '-':
                turtle.left(self.rotateAngle)
            elif char == '+':
                turtle.right(self.rotateAngle)
            elif char == '[':
                branchStack.append((turtle.position(), turtle.heading()))
            elif char == ']':
                turtle.penup()

                position, heading = branchStack.pop()
                turtle.goto(position)
                turtle.setheading(heading)

                turtle.pendown()

        turtle.screensize(10000, 10000)

        turtle.update()
        # turtle.mainloop()
        

system = LSystem("F", {"F": "F[+F][-F]F"}, 7, 25, 3)
system.generate(False)
system.draw()

turtle.penup()
turtle.right(90)
turtle.goto(400, 0)
turtle.pendown()

system = LSystem("F", {"F": "F[+F][-F]F"}, 7, 50, 3)
system.generate(False)
system.draw()

turtle.penup()
turtle.right(90)
turtle.goto(800, 0)
turtle.pendown()

system = LSystem("F", {"F": "F[+F][-F]F"}, 7, 75, 3)
system.generate(False)
system.draw()

turtle.mainloop()
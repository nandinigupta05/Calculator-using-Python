import re

print("Our Magical Calculator")
print("Type 'quit' to exit.")

previous=0
run=True

def doMath():
    global run
    global previous

    if previous==0:
        equation=input("Enter equation: ")
    else:
        equation=input(str(previous))

    if equation=='quit':
        print("Goodbye,human")
        run = False
    else:
        equation=re.sub('[a-zA-z,.:()" "]','',equation)

    if previous==0:
        previous=eval(equation)  #built in function to evaluate the equation
    else:
        previous=eval(str(previous)+equation)


while run:
    doMath()
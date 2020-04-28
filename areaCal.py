import math

def getTriangle():
    base = int(input("Enter Base: "))
    height = int(input("Enter Height: "))

    area = (base * height) / 2
    print("The area of the triangle is", area)

def getCircle():
    radius = int(input("Enter Radius: "))
    
    area = math.pi * (radius * radius)
    print("The area of the circle is", round(area, 3))

def getRectangle():
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))

    area = width * height
    print("The area of the square is", round(area, 2))

def getSquare():
    side = int(input("Enter Side: "))

    area = side * side
    print("The area of the square is", area)

def getParallelogram():
    base = int(input("Enter Base: "))
    height = int(input("Enter Height: "))

    area = base * height
    print("The area of the parallelogram is", area)

def getTrapezoid():
    top = int(input("Enter Top Side: "))
    bottom = int(input("Enter Bottom Side: "))
    height = int(input("Enter Height: "))

    area = 0.5 * (top + bottom) * height
    print("The area of the trapezoid is", area)

def findShape(shape):
    if shape == 'triangle':
        getTriangle()

    elif shape == 'circle':
        getCircle()

    elif shape == 'rectangle':
        getRectangle()

    elif shape == 'square':
        getSquare()

    elif shape == 'parallelogram':
        getParallelogram()

    elif shape == 'trapezoid':
        getTrapezoid()

shapeAmount = int(input("Enter Amount of Shapes: "))

if shapeAmount == 1:
    shape = input("Enter a Shape: ").lower()
    findShape(shape)

else:
    areaList = []

    for i in shapeAmount():
        shape = input("Enter a Shape: ").lower()
        areaList.append(sh)

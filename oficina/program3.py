def triangleArea (h, b):
    area = (h * b) / 2
    print(f"The triangle area of {b} base and {h} height is {area}")
### Program beggining:
height = float(input("Type the triangle height: "))
base = float(input("Type the triangle base: "))
triangleArea(height, base)
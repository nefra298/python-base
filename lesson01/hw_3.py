import math


def tonumeric(inp):
    try:
        val = int(inp)
        return val
    except ValueError:
        try:
            val = float(inp)
            return val
        except ValueError:
            val = None
            return val


print("Calculating the area of a circle")
inp1 = input("Enter a radius:")
r = tonumeric(inp1)
if r is not None:
    area = math.pi * r * r
    print("The area of a circle:", area)
else:
    print("Please use numeric values!")

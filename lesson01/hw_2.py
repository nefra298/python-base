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


print ("Calculating the area of a triangle")
inp1 = input("Enter the length of side A:")
inp2 = input("Enter the length of side B:")
inp3 = input("Enter the length of side C:")
a = tonumeric(inp1)
b = tonumeric(inp2)
c = tonumeric(inp3)
if (a is not None) and (b is not None) and (c is not None):
    if (a < b + c) and (b < a + c) and (c < a + b):
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("The area of a triangle:", area)
    else:
        print("No such triangle!")
else:
    print("Please use numeric values!")

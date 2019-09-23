def tonumber(inp):
    try:
        val = int(inp)
        return val
    except ValueError:
        try:
            val = float(inp)
            return val
        except ValueError:
            val=None
            return val
inp1=input("Type a number1:")
inp2=input("Type a number2:")
a=tonumber(inp1)
b=tonumber(inp2)
if (a is not None) and (b is not None):
    print(a*b)
else:
    print("NaN")
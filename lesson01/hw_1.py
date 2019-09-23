def ToNumeric(inp):
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
print ("Calculating the area of a rectangle")
inp1=input("Type a length:")
inp2=input("Type a width:")
a=ToNumeric(inp1)
b=ToNumeric(inp2)
if (a is not None) and (b is not None):
    print("The area of a rectangle:",a*b)
else:
    print("Please use numeric values!")

def greet(name,message="Hi"):
    return f"{message} {name}"

n=greet("Anmol","Hello")
print(n)

def subtract(x,y):
    ''' This function is about subtracting and positional arguments'''
    return x-y
print(subtract(5,10))
print(subtract.__doc__)